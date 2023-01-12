/*
Visual Computing 2022/2023
--------------------------
Samuel Silva, Oct. 2022

Vertex shader supporting per-fragment shading.
The shader just passes the position and normal in world coordinates. These wiil be interpolated by OpenGL
when passed to the fragment shader.

*/
#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;
layout (location = 2) in vec3 normal;

out vec3 vNormal;
out vec3 fragPos;

// Model view and projection matrices

uniform mat4 p3d_ModelViewMatrix;
uniform mat4 p3d_ProjectionMatrix;
uniform mat4 p3d_ModelMatrix;
uniform mat4 p3d_ViewMatrix;
uniform mat4 p3d_ViewProjectionMatrix;


uniform vec4 lightColor;

void main()
{
    fragPos = vec3(p3d_ModelMatrix *  vec4(position, 1.0));
    vNormal = mat3(transpose(inverse(p3d_ModelMatrix))) * normal;

    gl_Position = p3d_ProjectionMatrix * p3d_ViewMatrix * vec4(fragPos, 1.0);
}
