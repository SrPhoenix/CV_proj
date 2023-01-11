#version 330

uniform vec4 p3d_Color;

in vec3 v_normal;
in vec3 v_light;

out vec4 p3d_FragColor;

void main() {
  float diffuse = max(dot(v_normal, v_light), 0.0);
  p3d_FragColor = p3d_Color * diffuse;
}
