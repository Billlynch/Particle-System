typedef struct tag_vect3
{
  float x;
  float y;
  float z;
} vect3;

typedef struct tag_particle
{
  vect3 position;
  float s;
  vect3 target;
  double mass;
  vect3 speed;
  float life;
  int n_bounces;
  unsigned char r;
  unsigned char g;
  unsigned char b;
  unsigned char a;
} particle;

#define GRAVITY -9.81
#define FLOOR_Z -7.0

__kernel void simulate_particle(__global particle * particleArray, __global float * particleArrayToOpenGL, __global float * metaBuffer)
{
    size_t tid = get_global_id(0);


    if (metaBuffer[tid] > 0.0) {
    		vect3 acc;
    		acc.x = 0.0;
    		acc.y = 0.0;
    		acc.z = 0.0;
    		double speed_multiplier = 5.5f;

    		if (particleArrayToOpenGL[(tid * 4) + 2] <= FLOOR_Z) {
    			particleArrayToOpenGL[(tid * 4) + 2] = FLOOR_Z + 0.1;
    			acc.z = 5.0;
    			particleArray[tid].n_bounces++;
    		} else {
    			acc.z = GRAVITY;
    		}

    		float sx = acc.x * particleArray[tid].mass;
    		float sy = acc.y * particleArray[tid].mass;
    		float sz = acc.z * particleArray[tid].mass;

    		particleArrayToOpenGL[(tid * 4) + 0] += sx;
    		particleArrayToOpenGL[(tid * 4) + 1] += sy;
    		particleArrayToOpenGL[(tid * 4) + 2] += sz * 0.0016;
    		metaBuffer[tid] -= 0.1;
    } else {

            particleArrayToOpenGL[(tid * 4) + 3] = -1.0;

           if (metaBuffer[tid] < -5.0) {
                  particleArrayToOpenGL[(tid * 4) + 0] = particleArray[tid].position.x;
                  particleArrayToOpenGL[(tid * 4) + 1] = particleArray[tid].position.y;
                  particleArrayToOpenGL[(tid * 4) + 2] = particleArray[tid].position.z;
                  particleArrayToOpenGL[(tid * 4) + 3] = particleArray[tid].s;

                  metaBuffer[tid] = particleArray[tid].life;
            } else {
                metaBuffer[tid] -= 0.1;
            }
    }


}