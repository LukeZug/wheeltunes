$(document).ready(function() {
    $("#speed_input, #HR_input, #BN_input").change(function() {
      var speed = $("#speed_input").val();
      var heart_rate = $("#HR_input").val();
      var noise = $("#BN_input").val();
      $.ajax({
        url: "/wheeltunes/sliders/",
        type: "POST",
        data: {
            "speed": speed,
            "heart-rate": heart_rate,
            "background-noise": noise,
            csrfmiddlewaretoken:  $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function(data) {
            // The following code updates the page dynamically.

            // Update sensor data on the front end
            $("#speed_sensor").text(data['sensor_data']['speed']);
            $("#hr").text(data['sensor_data']['heart_rate']);
            $("#bg_noise").text(data['sensor_data']['background_noise']);

            // Update offsets on the front end
            $("#lower_offset").text(data['lower_offset']);
            $("#upper_offset").text(data['upper_offset']);

            // Update the playable songs displayed to users
            var playlist = $("#playlist");
            playlist.empty();

            for (i=0; i < data['playable_songs'].length; i++) {
                $("<li>").text(data['playable_songs'][i]).appendTo(playlist)
            }
        }
      });
    });
});  