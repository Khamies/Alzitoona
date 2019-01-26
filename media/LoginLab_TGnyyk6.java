public class LoginLab {


public static String login(String phone_number,String password)


{ public static String message;
 public static String url="127.0.0.1/midana/Login/" ;



StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                           new Response.Listener<String>()
                           {
                               @Override
                               public void onResponse(String response) {
                                   try {
                                       //response = response.substring(1,response.length()-1);
                                       JSONObject jsonResponse = new JSONObject(response);
                                     ArrayList<JSONObject> response=  Lab.parseResponse(jsonResponse)

                                     message=response.get(0).get(0);

                                  
                                       finish();
                                   } catch (JSONException e) {
                                       e.printStackTrace();
                                       Log.e("jsonagain",e.getMessage());
                                   }


                               }
                           },
                           new Response.ErrorListener()
                           {
                               @Override
                               public void onErrorResponse(VolleyError error) {
                                   // TODO Auto-generated method stub
                                   Log.d("ERROR","error => "+error.toString());
                               }
                           }
                   ) {
                       @Override
                       public Map<String, String> getParams() throws AuthFailureError {
                           Map<String, String>  params ;
                           params.put("phone_number",phone_number);
                           params.put("password",password);
                           
                           return params;
                       }
                   };
                   RequestQueue queue = Volley.newRequestQueue(getApplicationContext());
                   queue.add(postRequest);
                   queue.start();





                    return message;


}

}


