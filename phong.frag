/*
Visual Computing 2022/2023
--------------------------
Samuel Silva, Oct. 2022

Fragment shader implementing per-fragment shading

*/
#version 330

precision mediump float;

in vec3 vNormal;
in vec3 fragPos;

uniform vec4 lightPosition;
uniform vec3 viewerPosition;
uniform vec4 lightColor;

out vec4 out_color;

// these are properties of the OBJECT
    vec4 ambient;
    vec4 diffuse;
    vec4 specular;
    float shininess;


void main() {
    // ambient
    float ambientStrength = 0.2;
    vec4 ambient = ambientStrength * ambient * lightColor;

    // diffuse
    vec3 norm = normalize(vNormal); //interpolated normals might not be normalized

    vec3 lightDir;

    if (lightPosition[3] == 0.0) // directional lighting
        lightDir = normalize(lightPosition.xyz);
    else
        lightDir = normalize(lightPosition.xyz - fragPos);


    float diff = max(dot(norm, lightDir), 0.0);
    vec4 diffuse = diff * diffuse * lightColor;

    // specular
    float specularStrength = 0.8;
    vec3 viewDir = normalize(viewerPosition - fragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(-viewDir, reflectDir), 0.0), shininess/2);
    vec4 specular = specularStrength * spec * specular * lightColor;

    out_color = vec4(0.0, 1.0, 0.0, 1.0);

}