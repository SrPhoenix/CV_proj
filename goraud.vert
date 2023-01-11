#version 330

uniform mat4 p3d_ModelViewProjectionMatrix;

in vec3 p3d_Vertex;
in vec3 p3d_Normal;

out vec3 v_normal;
out vec3 v_light;

void main() {
  v_normal = normalize(p3d_Normal);
  v_light = vec3(0, 0, 1);
  gl_Position = p3d_ModelViewProjectionMatrix * vec4(p3d_Vertex, 1);
}
