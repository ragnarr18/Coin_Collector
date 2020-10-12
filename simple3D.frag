
// varying vec4 v_color;

// void main(void)
// {
//     gl_FragColor = v_color;
// }

varying vec4 v_normal;
varying vec4 v_s;
varying vec4 v_h;

varying vec4 v_normal1;
varying vec4 v_s1;
varying vec4 v_h1;

varying vec4 v_normal2;
varying vec4 v_s2;
varying vec4 v_h2;

uniform vec4 u_light_diffuse;
uniform vec4 u_light_specular;

uniform vec4 u_light_diffuse1;
uniform vec4 u_light_specular1;

uniform vec4 u_light_diffuse2;
uniform vec4 u_light_specular2;

uniform vec4 u_mat_diffuse;
uniform vec4 u_mat_specular;
uniform float u_mat_shininess;


void main(void)
{
	float lambert = max(dot(v_normal, v_s), 0);
	float phong = max(dot(v_normal, v_h), 0);

	gl_FragColor = u_light_diffuse * u_mat_diffuse * lambert
			+ u_light_specular * u_mat_specular * pow(phong, u_mat_shininess);
		
	float lambert1 = max(dot(v_normal, v_s1), 0);
	float phong1 = max(dot(v_normal, v_h1), 0);

	gl_FragColor += u_light_diffuse1 * u_mat_diffuse * lambert1
			+ u_light_specular1 * u_mat_specular * pow(phong1, u_mat_shininess); 

	float lambert2 = max(dot(v_normal, v_s2), 0);
	float phong2 = max(dot(v_normal, v_h2), 0);

	gl_FragColor += u_light_diffuse2 * u_mat_diffuse * lambert2
			+ u_light_specular2 * u_mat_specular * pow(phong2, u_mat_shininess); 
}