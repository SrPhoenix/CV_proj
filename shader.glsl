#version 330
// Vertex shader
void main() {
  // Vertex processing code goes here
}

// Fragment shader
void main() {
  #define MAX_LIGHTS 8

  uniform vec3 diffuseColor;
  uniform vec3 specularColor;
  uniform float shininess;

  struct Light {
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
  };

  uniform Light lights[MAX_LIGHTS];
  uniform int numLights;

  in vec3 vNormal;
  in vec3 vViewPosition;

  out vec4 fragColor;

  void main() {
    // Initialize the final color to the ambient light of the scene
    vec3 color = vec3(0.0);

    for (int i = 0; i < numLights; i++) {
      Light light = lights[i];
      vec3 lightPosition = light.position;

      // Calculate the vector from the surface point to the light source
      vec3 lightVector = normalize(lightPosition - vViewPosition);

      // Calculate the diffuse contribution
      float diffuseContribution = max(dot(vNormal, lightVector), 0.0);
      color += diffuseColor * light.diffuse * diffuseContribution;

      // Calculate the specular contribution
      vec3 reflectVector = reflect(-lightVector, vNormal);
      vec3 viewVector = normalize(vViewPosition);
      float specularContribution = pow(max(dot(reflectVector, viewVector), 0.0), shininess);
      color += specularColor * light.specular * specularContribution;
    }

    fragColor = vec4(color, 1.0);
  }