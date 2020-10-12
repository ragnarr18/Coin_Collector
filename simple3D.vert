// attribute vec3 a_position;
// attribute vec3 a_normal;

// uniform mat4 u_model_matrix;		//4x4 matrix
// uniform mat4 u_view_matrix;
// uniform mat4 u_projection_matrix;

// uniform vec4 u_color;     //4dimensional vector

// varying vec4 v_color;  //Leave the varying variables alone to begin with

// void main(void)
// {
// 	vec4 position = vec4(a_position.x, a_position.y, a_position.z, 1.0);
// 	vec4 normal = vec4(a_normal.x, a_normal.y, a_normal.z, 0.0);
	


// 	//local coordinates are here
// 	position = u_model_matrix * position;
// 	normal = u_model_matrix * normal;

// 	//global coordinates are here
// 	float light_factor_1 = max(dot(normalize(normal), normalize(vec4(1, 2, 3, 0))), 0.0);
// 	float light_factor_2 = max(dot(normalize(normal), normalize(vec4(-3, -2, -1, 0))), 0.0);
// 	v_color = (light_factor_1 + light_factor_2) * u_color; // ### --- Change this vector (pure white) to color variable --- #####

// 	//eye coordinates
// 	position = u_view_matrix * position;
	
// 	//clip coordinates
// 	position = u_projection_matrix * position;
	
// 	gl_Position = position;
// }

attribute vec3 a_position;
attribute vec3 a_normal;

uniform mat4 u_model_matrix;		//4x4 matrix
uniform mat4 u_view_matrix;
uniform mat4 u_projection_matrix;

// uniform vec4 u_color;     //4dimensional vector
uniform vec4 u_eye_position;

uniform vec4 u_light_position;
uniform vec4 u_light_position1;
uniform vec4 u_light_position2;


// uniform vec4 u_light_diffuse;
// uniform vec4 u_light_specular;

// uniform vec4 u_mat_diffuse;
// uniform vec4 u_mat_specular;
// uniform float u_mat_shininess;

// varying vec4 v_color;  //Leave the varying variables alone to begin with
varying vec4 v_normal;
varying vec4 v_s;
varying vec4 v_h;

varying vec4 v_normal1;
varying vec4 v_s1;
varying vec4 v_h1;

varying vec4 v_normal2;
varying vec4 v_s2;
varying vec4 v_h2;

void main(void)
{
	vec4 position = vec4(a_position.x, a_position.y, a_position.z, 1.0);
	vec4 normal = vec4(a_normal.x, a_normal.y, a_normal.z, 0.0);
	
	//local coordinates are here
	position = u_model_matrix * position;
	v_normal = normalize(u_model_matrix * normal);

	//global coordinates are here
	v_s = normalize(u_light_position - position); //vector im going, to the light
	v_s1 = normalize(u_light_position1 - position);
	v_s2 = normalize(u_light_position2 - position);
	// v_color = u_light_diffuse * u_mat_diffuse * lambert; // takes one dimension of every component and returns that certain dimension(takes all X => set an x value)
	
	//can also be done like this:
	// v_color.r = u_light_diffuse.r * u_mat_diffuse.r * lambert;
	// v_color.g = u_light_diffuse.g * u_mat_diffuse.g * lambert;
	// v_color.b = u_light_diffuse.b * u_mat_diffuse.b * lambert;

	vec4 v = normalize(u_eye_position - position);
	v_h = normalize(v_s + v);
	v_h1 = normalize(v_s1 + v);
	v_h2 = normalize(v_s2 + v);
	
	// float light_factor_1 = max(dot(normalize(normal), normalize(vec4(1, 2, 3, 0))), 0.0);
	// float light_factor_2 = max(dot(normalize(normal), normalize(vec4(-3, -2, -1, 0))), 0.0);
	// v_color = (light_factor_1 + light_factor_2) * u_color; // ### --- Change this vector (pure white) to color variable --- #####

	//eye coordinates
	position = u_view_matrix * position;
	
	//clip coordinates
	position = u_projection_matrix * position;
	
	gl_Position = position;
}