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

            // Don't remove the currently playing song from the DOM! or else...
            if (currentlyPlayingAudio) {
              var currentAudioId = currentlyPlayingAudio.id;
              playlist.children("audio").each(function() {
                var audioId = $(this).attr("id");
                if (audioId !== currentAudioId) {
                  $(this).remove();
                }
              });
            } else {
              playlist.empty();
            }

            for (i=0; i < data['playable_songs'].length; i++) {
              if (currentlyPlayingAudio) {
                if (currentlyPlayingAudio.id == "audio_" + data['playable_songs'][i]['id']) {
                  continue;
                }
              }

                $("<audio>", {
                  'class': 'audio',
                  'id': 'audio_' + data['playable_songs'][i]['id'],
                  'src': data['playable_songs'][i]['static_url'],
                  'onplay': "setNowPlaying('" + data['playable_songs'][i]['title'] + " by " + data['playable_songs'][i]['artist'] + "')",
                  'onended': "playNextSong()"
                }).appendTo(playlist);
            }

            if (currentlyPlayingAudio) {
              // Boost volume to 1 if louder than 60db (cycling in a city/busy road)
              // Otherwise keep on 0.5
              // Can be changed as needed!

              var bg_db = data['sensor_data']['background_noise'];
              if (bg_db >= 60) {
                currentlyPlayingAudio.volume = 1;
              } else {
                currentlyPlayingAudio.volume = 0.5;
              }
            }
        }
      });
    });
});  