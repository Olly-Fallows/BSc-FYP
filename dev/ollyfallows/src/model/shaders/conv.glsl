#version 430 core

// Series of definitions whos values are replaced before compilation

#define H SIZE_H

#define IN_X IN_SIZE_X
#define IN_Y IN_SIZE_Y
#define IN_Z IN_SIZE_Z

#define KERNEL_X KERNEL_SIZE_X
#define KERNEL_Y KERNEL_SIZE_Y
#define KERNEL_Z KERNEL_SIZE_Z

#define OUT_X OUT_SIZE_X
#define OUT_Y OUT_SIZE_Y
#define OUT_Z OUT_SIZE_Z

#define EDGE EDGE_HANDLING
// 0 -> null handling
// 1 -> ignore edge
// 2 -> pad with 0
// 3 -> pad with 1
#define STEP 1

// Set how many workers per group
layout(local_size_x=OUT_X, local_size_y=OUT_Y, local_size_z=OUT_Z) in;

// Input buffer for the data from the previous layer
layout(std430, binding=0) buffer in_0
{
  float in_buffer[1];
};

// Input buffer for the kernel to be used
layout(std430, binding=1) buffer kernel_0
{
  float kernel_buffer[1];
};

// Output buffer for the result of the convolution
layout(std430, binding=2) buffer out_0
{
  float out_buffer[1];
};

// Function to convert a 3d coord to a 1d coord for the output buffer`
int outPos(float x, float y, float z) {
  return int(x + y*OUT_X + z*OUT_X*H);
}

// Function to convert a 3d coord to a 1d coord for the input buffer`
int inPos(float x, float y, float z) {
  return int(x + y*IN_X + z*IN_X*IN_Y);
}

// Function to convert a 3d coord to a 1d coord for the kernel buffer
int kernelPos(float x, float y, float z){
  return int(x + y*KERNEL_X + z*KERNEL_X*KERNEL_Y);
}

// Function to calculate the value of one element of the output buffer`
float applyKernel(int x, int y) {
  // Variable to keep a running total for calculating the avg
  float val = 0;
  // Variable to track how many elements where used for the avg
  int cellCount = 0;
  // Series of nested for loops to iterate throw the elements of the kernel
  for (int a=0; a<KERNEL_X; a++) {
    // Convert the kernel x position to a position on the input buffer
    int xpos = a+x-(KERNEL_X-1)/2;
    // Perform edge handling for if that x position doesn't lie within the input
    // buffer.
    if (xpos < 0 || xpos > IN_X) {
      switch (EDGE) {
      case 0:
        return 0;
      case 1:
        continue;
      case 2:
        cellCount++;
        continue;
      case 3:
        val += 1;
        cellCount++;
        continue;
      }
    }
    // Same as the x position for loop
    for (int b=0; b<KERNEL_Y; b++) {
      int ypos = b+y-(KERNEL_Y-1)/2;
      if (ypos < 0 || ypos > IN_Y) {
        switch (EDGE) {
        case 0:
          return 0;
        case 1:
          continue;
        case 2:
          cellCount++;
          continue;
        case 3:
          val += 1;
          cellCount++;
          continue;
        }
      }
      // For loop for the z coord
      for (int c=0; c<KERNEL_Z; c++) {
        // Adds the product of the input buffer element and the kernel element
        // to the running total.
        val += kernel_buffer[kernelPos(a, b, c)] *
               in_buffer[inPos(xpos, ypos, c)];
        cellCount++;
      }
    }
  }
  // Returns the avg for the output.
  return val/cellCount;
}

void main() {
  // Get the output buffer coords as the local worker index and the group index
  vec2 coords = vec2(gl_LocalInvocationID.x, gl_WorkGroupID.x);
  int xoffset = 0;
  int yoffset = 0;
  // Adjust the offset if using case 0 of edge handling
  if (EDGE == 0) {
    xoffset = int((KERNEL_X-1)/2);
    yoffset = int((KERNEL_Y-1)/2);
  }
  // Calculate the coords to center the kernel over for the input buffer
  int x = int(coords.x*STEP)+xoffset;
  int y = int(coords.y*STEP)+yoffset;
  // Put the result of the convolution into the output buffer
  out_buffer[outPos(coords.x,coords.y,0)] = applyKernel(x,y);
}
