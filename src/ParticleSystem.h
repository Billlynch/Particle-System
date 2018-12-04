//
// Created by Bill Lynch on 15/10/2018.
//

#ifndef GRAPHICS_PARTICLESYSTEM_H
#define GRAPHICS_PARTICLESYSTEM_H
#define GLM_ENABLE_EXPERIMENTAL

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <glm/gtx/norm.hpp>
#include <vector>
#include <glm/glm.hpp>
#include <string>
#include "common/Particle.h"
#include "common/file_loader.h"
#include "common/shader.hpp"
#include "common/controls.hpp"
#include "Analyser.h"
#include <algorithm>
#include <cstdlib>
#include <ctime>

#ifdef __APPLE__
#include <OpenCL/opencl.h>
#else

#include <CL/cl.hpp>

#endif


using namespace glm;

#define NUM_PARTICLES 3008000
#define GRAVITY -9.81
#define FLOOR_Z -7.0


inline void checkErr(cl_int err, const char *name) {
    if (err != CL_SUCCESS) {
        std::cerr << "Error: " << name << ": " << err << std::endl;
        exit(EXIT_FAILURE);
    }
}


class ParticleSystem {
private:
    GLFWwindow *window{};
    int height = 768 * 2;
    int width = 1024 * 2;
    std::vector<vec3 *> objVectors;
    particle particlesContainer[NUM_PARTICLES]{};
    bool *spaceHeld = new bool(false);
    double frameInitTime{}, prePhysicsTime{}, postPhysicsTime{}, postLoadIntoOpenGLBuffersTime{}, postDrawCallTime{}, delta{};
    double lastTime{};
    unsigned long frameCount = 0;
    mat4 ProjectionMatrix, ViewMatrix, ViewProjectionMatrix;
    vec3 CameraPosition;
    Analyser *analyser{};
    float particleMetaDataBuffer[NUM_PARTICLES]{};
    GLint CameraRight_worldspace_ID{}, CameraUp_worldspace_ID{}, ViewProjMatrixID{};
    cl::Event event, writeEvent;
    cl::CommandQueue queue, writeQueue;
    cl::Buffer kernelParticleBuffer, kernelParticleBufferToOpenGl, kernelParticleMetaBuffer, kernelSpaceBuffer;
    cl::Kernel kernel;
    float *particle_position_size_data = new float[NUM_PARTICLES * 4];
    GLubyte *particle_colour_data = new GLubyte[NUM_PARTICLES * 4];
    GLuint particles_color_buffer{}, VertexArrayID{}, particles_position_buffer{}, base_mesh_vertex_buffer{};


    void mainLoop();

    void generateBuffers(GLuint &base_mesh_vertex_buffer,
                         GLuint &particles_position_buffer,
                         GLuint &particles_color_buffer);

    void simParticles();

    void simParticlesOpenCL();

    void generateNewParticles();

    void setupVertexShaderInputs(GLuint billboard_vertex_buffer,
                                 GLuint particles_position_buffer,
                                 GLuint particles_color_buffer);

    int setupGLEWandGLFW();

public:
    GLuint programID{};

    ParticleSystem() {
        srand(static_cast<unsigned>(time(0)));
    };

    ~ParticleSystem() = default;


    void runParticleSystem(std::string &fileName);

    void loadObj(std::string &fileName);

    void cleanUpBuffers() const;

    bool isWindowClosed();

    void setupBuffers();

    void setupShaders();

    void calculateFrameDelta();

    void loadDataIntoBuffers() const;

    void setupOpenCl();
};


#endif //GRAPHICS_PARTICLESYSTEM_H
