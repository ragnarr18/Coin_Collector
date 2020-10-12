attribute vec3 a_position;
attribute vec3 a_normal;
uniform mat4 u_model_matrix;
uniform mat4 u_view_matrix;
uniform mat4 u_projection_matrix;
uniform vec4 u_light_position;
uniform vec4 u_light_position1;
uniform vec4 u_light_position2;
uniform vec4 u_eye_position;

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
	v_s = normalize(u_light_position - position);
	v_s1 = normalize(u_light_position1 - position);
	v_s2 = normalize(u_light_position2 - position);

	vec4 v = normalize(u_eye_position - position);
	v_h = normalize(v_s + v);
	v_h1 = normalize(v_s1 + v);
	v_h2 = normalize(v_s2 + v);

	//eye coordinates
	position = u_view_matrix * position;
	
	//clip coordinates
	position = u_projection_matrix * position;
	
	gl_Position = position;
}