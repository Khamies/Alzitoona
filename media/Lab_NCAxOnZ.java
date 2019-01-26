
public class Lab {

public static ArrayList<JSONObject> parseResponse(String response) throws JSONException {
      ArrayList<JSONObject> result = new ArrayList();
      response=response.substring(1,response.length()-1);
      while (response.length()!=0){            JSONObject object = new JSONObject(response.substring(0,response.indexOf("}")+1));
          if (response.indexOf("}")+2<=response.length()) {
              response = response.substring(response.indexOf("}")+2);
          } else {
              response = response.substring(response.indexOf("}")+1);
          }
          result.add(object);
      }
      return result;}





public static Midan midan (JSONObject object) throws JSONException {
      Midan user = new Midan();
      user.setId(object.getString(" Owner"));
      user.setName(object.getString("name"));
      user.setPrice(object.getString("price"));
      user.setSize(object.getString("size"));
      user.setTelephne(object.getString("telephone"));
      double latidute = object.getDouble("latidute");
      double longtude = object.getDouble("longitude");
      LatLng latLng = new LatLng(latidute,longtude)
      user.setStoreLocation(latLng);
      user.setId(object.getString("available"));
      user.setId(object.getString("city"));
      user.setId(object.getString("suits"));
      user.setId(object.getString("water"));
      user.setId(object.getString("bathroom"));
      user.setId(object.getString(" ball"));
      user.setId(object.getString("photo_1"));
      user.setId(object.getString("photo_2"));
      user.setId(object.getString("photo_3"));

      return user;
  
  }


   

}























  }    public static Product parseProduct(JSONObject object) throws JSONException {
      Product p = new Product();
      p.setId(object.getString("id"));
      p.setDescription(object.getString("description"));
      p.setStatus(object.getInt("status"));
      String downvotes = object.getString("downvotes");
      p.setDownVotes("".equals(downvotes)?0:downvotes.split(",").length);
      String upvotes = object.getString("upvotes");
      p.setUpVotes("".equals(upvotes)?0:upvotes.split(",").length);
      p.setImages(object.getString("images"));
      p.setPrice(object.getInt("price"));
      p.setPurchaseDate(new Date());
      p.setName(object.getString("name"));
      p.setUploader(object.getString("user"));
      p.setStoreName(object.getString("store_name"));
      p.setStorePlace(object.getString("place_store"));
      p.setRating((float) object.getDouble("rating"));
      double latidute = object.getDouble("latidute");
      double longtude = object.getDouble("longitude");
      LatLng latLng = new LatLng(latidute,longtude);
      p.setStoreLocation(latLng);
      return p;
  }