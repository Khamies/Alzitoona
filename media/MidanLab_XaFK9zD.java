public class MidanLab {


public static ArrayList<Midan> getMidansAccordingToState(String state)


{ public static String Message;
 public static String url="127.0.0.1/midana/MidanState/" ;
 public static ArrayList <Midan> All_Midans;



StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                           new Response.Listener<String>()
                           {
                               @Override
                               public void onResponse(String response) {
                                   try {
                                       //response = response.substring(1,response.length()-1);
                                       JSONObject jsonResponse = new JSONObject(response);
                                     ArrayList<JSONObject> response=  Lab.parseResponse(jsonResponse)

                                    for(JSONObject object:response){

                                      Midan midan=Lab.midan(object);
                                      All_Midans.add(midan);
                                    }
                                     

                                  
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
                           params.put("state",state);
                           
                           return params;
                       }
                   };
                   RequestQueue queue = Volley.newRequestQueue(getApplicationContext());
                   queue.add(postRequest);
                   queue.start();





                    return All_Midans;

}


}


