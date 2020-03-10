#version 430 core

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

layout(local_size_x=OUT_X, local_size_y=OUT_Y, local_size_z=OUT_Z) in;

layout(std430, binding=0) buffer in_0
{
  float in_buffer[1];
};
layout(std430, binding=1) buffer kernel_0
{
  float kernel_buffer[1];
};
layout(std430, binding=2) buffer out_0
{
  float out_buffer[1];
};

int outPos(float x, float y, float z) {
  return int(x + y*OUT_X + z*OUT_X*H);
}
int inPos(float x, float y, float z) {
  return int(x + y*IN_X + z*IN_X*IN_Y);
}
int kernelPos(float x, float y, float z){
  return int(x + y*KERNEL_X + z*KERNEL_X*KERNEL_Y);
}
float applyKernel(int x, int y) {
  float val = 0;
  int cellCount = 0;
  for (int a=0; a<KERNEL_X; a++) {
    int xpos = a+x-(KERNEL_X-1)/2;
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
      for (int c=0; c<KERNEL_Z; c++) {
        val += kernel_buffer[kernelPos(a, b, c)] *
               in_buffer[inPos(xpos, ypos, c)];
        cellCount++;
      }
    }
  }
  return val/cellCount;
}

void main() {
  vec2 coords = vec2(gl_LocalInvocationID.x, gl_WorkGroupID.x);
  int xoffset = 0;
  int yoffset = 0;
  if (EDGE == 0) {
    xoffset = int((KERNEL_X-1)/2);
    yoffset = int((KERNEL_Y-1)/2);
  }
  int x = int(coords.x*STEP)+xoffset;
  int y = int(coords.y*STEP)+yoffset;
  out_buffer[outPos(coords.x,coords.y,0)] = applyKernel(x,y);
}
