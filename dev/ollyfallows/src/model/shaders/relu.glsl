#version 430 core

#define IN_X IN_SIZE_X
#define IN_Y IN_SIZE_Y
#define IN_Z IN_SIZE_Z

#define OUT_X OUT_SIZE_X
#define OUT_Y OUT_SIZE_Y
#define OUT_Z OUT_SIZE_Z

layout(local_size_x=OUT_X, local_size_y=OUT_Y, local_size_z=OUT_Z) in;

layout(std430, binding=0) buffer in_0
{
  float in_buffer[1];
};
layout(std430, binding=1) buffer out_0
{
  float out_buffer[1];
};

void main(){
  const uint frag_i = gl_LocalInvocationID.x + gl_LocalInvocationID.y*OUT_X +
                      gl_LocalInvocationID.z*OUT_X*OUT_Y;
  out_buffer[frag_i] = in_buffer[frag_i];
  if (out_buffer[frag_i] < 0){
    out_buffer[frag_i] = 0;
  }
}
