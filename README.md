# yanshee_openadk
## Overview 
 
Yan ADK is designed for the users that they can build their own application very quickly. 
Yan ADK provided two features: 

- Easy way to call API. 
- Easy way to receive the data from remote device.  

## Requirements. 
Python 2.7 or 3.4+ 

## Installation & Usage
 You can install Yan ADK from github. 
 
 ``` pip install git+https://github.com/UBTEDU/Yanshee_YanADK.git ``` 
 
(you may need to run pip with root permission: sudo pip install git+https://github.com/UBTEDU/Yanshee_YanADK.git) 

Then import the package: 


``` import openadk ``` 

## Setuptools 

Install via [Setuptools](https://pypi.org/project/setuptools/). 

``` python setup.py install --user ``` 

(or sudo python setup.py install to install the package for all users) 

Then import the package: 
``` import openadk ``` 

## Getting Started 

Please follow the installation procedure and then run the following: 

``` 
from __future__ 
import print_function 
import time 
import openadk from openadk.rest 
import ApiException from pprint 
import pprint  

# create an instance of the API class 
configuration = openadk.Configuration() 
configuration.host = 'http://<ip>:9090/v1' 
api_instance = openadk.DevicesApi(openadk.ApiClient(configuration))  
try:  
# Get system's battery information  
    api_response = api_instance.get_devices_battery()  
    pprint(api_response) 
except ApiException as e:  
    print(\"Exception when calling DevicesApi->get_devices_battery: %s \" % e) 
``` 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openadk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openadk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi(openadk.ApiClient(configuration))

try:
    # Get the battery information
    api_response = api_instance.get_devices_battery()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_battery: %s\n" % e)

```


## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:10101/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DevicesApi* | [**get_devices_battery**](docs/DevicesApi.md#get_devices_battery) | **GET** /devices/battery | Get the battery information
*DevicesApi* | [**get_devices_fall_management**](docs/DevicesApi.md#get_devices_fall_management) | **GET** /devices/fall_management | Get fall management configuration
*DevicesApi* | [**get_devices_languages**](docs/DevicesApi.md#get_devices_languages) | **GET** /devices/languages | Get language settings
*DevicesApi* | [**get_devices_led**](docs/DevicesApi.md#get_devices_led) | **GET** /devices/led | Get the light effects
*DevicesApi* | [**get_devices_versions**](docs/DevicesApi.md#get_devices_versions) | **GET** /devices/versions | Get the system versions
*DevicesApi* | [**get_devices_volume**](docs/DevicesApi.md#get_devices_volume) | **GET** /devices/volume | Get the volume
*DevicesApi* | [**put_devices_fall_management**](docs/DevicesApi.md#put_devices_fall_management) | **PUT** /devices/fall_management | Set fall management configuration
*DevicesApi* | [**put_devices_languages**](docs/DevicesApi.md#put_devices_languages) | **PUT** /devices/languages | Set language settings
*DevicesApi* | [**put_devices_led**](docs/DevicesApi.md#put_devices_led) | **PUT** /devices/led | Set the light effects
*DevicesApi* | [**put_devices_volume**](docs/DevicesApi.md#put_devices_volume) | **PUT** /devices/volume | Set the volume
*MediaApi* | [**delete_media_music**](docs/MediaApi.md#delete_media_music) | **DELETE** /media/music | Delete uploaded music
*MediaApi* | [**get_media_music**](docs/MediaApi.md#get_media_music) | **GET** /media/music | Get the music playing status
*MediaApi* | [**get_media_music_list**](docs/MediaApi.md#get_media_music_list) | **GET** /media/music/list | Get the music list
*MediaApi* | [**post_media_music**](docs/MediaApi.md#post_media_music) | **POST** /media/music | Upload music
*MediaApi* | [**put_media_music**](docs/MediaApi.md#put_media_music) | **PUT** /media/music | Start or stop music
*MotionsApi* | [**delete_motions_music**](docs/MotionsApi.md#delete_motions_music) | **DELETE** /motions | Delete motion files
*MotionsApi* | [**get_motions**](docs/MotionsApi.md#get_motions) | **GET** /motions | Get the current motions&#39; status
*MotionsApi* | [**get_motions_list**](docs/MotionsApi.md#get_motions_list) | **GET** /motions/list | Get all the motions&#39; name
*MotionsApi* | [**post_motions**](docs/MotionsApi.md#post_motions) | **POST** /motions | Upload motion files
*MotionsApi* | [**put_motions**](docs/MotionsApi.md#put_motions) | **PUT** /motions | Update the motions
*SensorsApi* | [**get_sensors_environment**](docs/SensorsApi.md#get_sensors_environment) | **GET** /sensors/environment | Get enviornment sensor&#39;s value
*SensorsApi* | [**get_sensors_gyro**](docs/SensorsApi.md#get_sensors_gyro) | **GET** /sensors/gyro | Get gyroscope sensor&#39;s value
*SensorsApi* | [**get_sensors_infrared**](docs/SensorsApi.md#get_sensors_infrared) | **GET** /sensors/infrared | Get infrared sensor&#39;s value
*SensorsApi* | [**get_sensors_list**](docs/SensorsApi.md#get_sensors_list) | **GET** /sensors/list | Get all sensors&#39; list
*SensorsApi* | [**get_sensors_pressure**](docs/SensorsApi.md#get_sensors_pressure) | **GET** /sensors/pressure | Get pressure sensor&#39;s value
*SensorsApi* | [**get_sensors_touch**](docs/SensorsApi.md#get_sensors_touch) | **GET** /sensors/touch | Get touch sensor&#39;s value
*SensorsApi* | [**get_sensors_ultrasonic**](docs/SensorsApi.md#get_sensors_ultrasonic) | **GET** /sensors/ultrasonic | Get ultrasonic sensor&#39;s value
*SensorsApi* | [**put_sensors**](docs/SensorsApi.md#put_sensors) | **PUT** /sensors | Calibrate sensor or change sensor&#39;s I2C address
*ServosApi* | [**get_servos_angles**](docs/ServosApi.md#get_servos_angles) | **GET** /servos/angles | Get servos&#39; angle
*ServosApi* | [**get_servos_mode**](docs/ServosApi.md#get_servos_mode) | **GET** /servos/mode | Get servos working mode
*ServosApi* | [**put_servos_angles**](docs/ServosApi.md#put_servos_angles) | **PUT** /servos/angles | Set servos&#39; angle
*ServosApi* | [**put_servos_mode**](docs/ServosApi.md#put_servos_mode) | **PUT** /servos/mode | Set the servos working mode
*SubscriptionsApi* | [**delete_motions_subscription**](docs/SubscriptionsApi.md#delete_motions_subscription) | **DELETE** /subscriptions/motions | Unsubscribe the motion status
*SubscriptionsApi* | [**delete_sensors_subscription**](docs/SubscriptionsApi.md#delete_sensors_subscription) | **DELETE** /subscriptions/sensors | Unsubscribe the sensor&#39;s value
*SubscriptionsApi* | [**delete_visions_subscription**](docs/SubscriptionsApi.md#delete_visions_subscription) | **DELETE** /subscriptions/visions | Unsubscribe compute vision result
*SubscriptionsApi* | [**delete_voice_asr_subscription**](docs/SubscriptionsApi.md#delete_voice_asr_subscription) | **DELETE** /subscriptions/voice/asr | Unsubscribe auto speech recognition result
*SubscriptionsApi* | [**delete_voice_iat_subscription**](docs/SubscriptionsApi.md#delete_voice_iat_subscription) | **DELETE** /subscriptions/voice/iat | Unsubscribe auto transform result
*SubscriptionsApi* | [**delete_voice_tts_subscription**](docs/SubscriptionsApi.md#delete_voice_tts_subscription) | **DELETE** /subscriptions/voice/tts | Unsubscribe text to speech result
*SubscriptionsApi* | [**post_motions_subscription**](docs/SubscriptionsApi.md#post_motions_subscription) | **POST** /subscriptions/motions | Subscribe the motion status
*SubscriptionsApi* | [**post_sensors_subscription**](docs/SubscriptionsApi.md#post_sensors_subscription) | **POST** /subscriptions/sensors | Subscribe the sensor&#39;s value
*SubscriptionsApi* | [**post_visions_subscription**](docs/SubscriptionsApi.md#post_visions_subscription) | **POST** /subscriptions/visions | Subscribe compute vision result
*SubscriptionsApi* | [**post_voice_asr_subscriptions**](docs/SubscriptionsApi.md#post_voice_asr_subscriptions) | **POST** /subscriptions/voice/asr | Subscribe auto speech recognition result
*SubscriptionsApi* | [**post_voice_iat_subscription**](docs/SubscriptionsApi.md#post_voice_iat_subscription) | **POST** /subscriptions/voice/iat | Subscribe auto transform result
*SubscriptionsApi* | [**post_voice_tts_subscriptions**](docs/SubscriptionsApi.md#post_voice_tts_subscriptions) | **POST** /subscriptions/voice/tts | Subscribe text to speech result
*VisionsApi* | [**delete_vision_photo**](docs/VisionsApi.md#delete_vision_photo) | **DELETE** /visions/photos | Delete a photo based the name
*VisionsApi* | [**delete_vision_photo_samples**](docs/VisionsApi.md#delete_vision_photo_samples) | **DELETE** /visions/photosamples | Delete the uploaded sample
*VisionsApi* | [**delete_visions_streams**](docs/VisionsApi.md#delete_visions_streams) | **DELETE** /visions/streams | Turn off the web stream for the camera
*VisionsApi* | [**delete_visions_tags**](docs/VisionsApi.md#delete_visions_tags) | **DELETE** /visions/tags | Delete a sample&#39;s tag based the tag name
*VisionsApi* | [**get_photo_samples**](docs/VisionsApi.md#get_photo_samples) | **GET** /visions/photosamples | Get all the uploaded photo samples
*VisionsApi* | [**get_vision**](docs/VisionsApi.md#get_vision) | **GET** /visions | Get compute vision result
*VisionsApi* | [**get_visions_photos**](docs/VisionsApi.md#get_visions_photos) | **GET** /visions/photos | Get a specific photo based the name
*VisionsApi* | [**get_visions_photos_lists**](docs/VisionsApi.md#get_visions_photos_lists) | **GET** /visions/photos/list | Get the photo&#39;s list
*VisionsApi* | [**get_visions_tags**](docs/VisionsApi.md#get_visions_tags) | **GET** /visions/tags | Get all the tag list
*VisionsApi* | [**post_vision_photo**](docs/VisionsApi.md#post_vision_photo) | **POST** /visions/photos | Take a photo
*VisionsApi* | [**post_visions_photo_samples**](docs/VisionsApi.md#post_visions_photo_samples) | **POST** /visions/photosamples | Upload photo sample
*VisionsApi* | [**post_visions_streams**](docs/VisionsApi.md#post_visions_streams) | **POST** /visions/streams | Turn on the web stream for the camera
*VisionsApi* | [**put_visions**](docs/VisionsApi.md#put_visions) | **PUT** /visions | Start or stop a compute vision task
*VisionsApi* | [**put_visions_tags**](docs/VisionsApi.md#put_visions_tags) | **PUT** /visions/tags | Set the sample&#39;s tag
*VoiceApi* | [**delete_voice_asr**](docs/VoiceApi.md#delete_voice_asr) | **DELETE** /voice/asr | Stop automatic speech recognition
*VoiceApi* | [**delete_voice_iat**](docs/VoiceApi.md#delete_voice_iat) | **DELETE** /voice/iat | Stop auto transform
*VoiceApi* | [**delete_voice_offline_syntax**](docs/VoiceApi.md#delete_voice_offline_syntax) | **DELETE** /voice/asr/offlinesyntax | Delete a offline grammar based offline grammar&#39;s name
*VoiceApi* | [**delete_voice_tts**](docs/VoiceApi.md#delete_voice_tts) | **DELETE** /voice/tts | Stop all text to speech
*VoiceApi* | [**get_voice_asr**](docs/VoiceApi.md#get_voice_asr) | **GET** /voice/asr | Get automatic speech recognition working status
*VoiceApi* | [**get_voice_iat**](docs/VoiceApi.md#get_voice_iat) | **GET** /voice/iat | Get auto transform(iat) result
*VoiceApi* | [**get_voice_offline_syntax**](docs/VoiceApi.md#get_voice_offline_syntax) | **GET** /voice/asr/offlinesyntax | Get offline grammar configuration
*VoiceApi* | [**get_voice_offline_syntax_grammars**](docs/VoiceApi.md#get_voice_offline_syntax_grammars) | **GET** /voice/asr/offlinesyntax/grammars | Get offline grammars&#39; name
*VoiceApi* | [**get_voice_tts**](docs/VoiceApi.md#get_voice_tts) | **GET** /voice/tts | Get specified or current working status
*VoiceApi* | [**post_voice_offline_syntax**](docs/VoiceApi.md#post_voice_offline_syntax) | **POST** /voice/asr/offlinesyntax | Add a new offline grammar
*VoiceApi* | [**put_voice_asr**](docs/VoiceApi.md#put_voice_asr) | **PUT** /voice/asr | Start automatic speech recognition
*VoiceApi* | [**put_voice_iat**](docs/VoiceApi.md#put_voice_iat) | **PUT** /voice/iat | Start auto transform
*VoiceApi* | [**put_voice_offline_syntax**](docs/VoiceApi.md#put_voice_offline_syntax) | **PUT** /voice/asr/offlinesyntax | Update offline grammar based grammar&#39;s name
*VoiceApi* | [**put_voice_tts**](docs/VoiceApi.md#put_voice_tts) | **PUT** /voice/tts | Start text to speech


## Documentation For Models

 - [CommonResponse](docs/CommonResponse.md)
 - [DevicesBattery](docs/DevicesBattery.md)
 - [DevicesBatteryResponse](docs/DevicesBatteryResponse.md)
 - [DevicesFallManagement](docs/DevicesFallManagement.md)
 - [DevicesFallManagementResponse](docs/DevicesFallManagementResponse.md)
 - [DevicesLED](docs/DevicesLED.md)
 - [DevicesLEDResponse](docs/DevicesLEDResponse.md)
 - [DevicesLanguage](docs/DevicesLanguage.md)
 - [DevicesLanguageResponse](docs/DevicesLanguageResponse.md)
 - [DevicesVersions](docs/DevicesVersions.md)
 - [DevicesVersionsResponse](docs/DevicesVersionsResponse.md)
 - [DevicesVolume](docs/DevicesVolume.md)
 - [DevicesVolumeResponse](docs/DevicesVolumeResponse.md)
 - [MediaMusicList](docs/MediaMusicList.md)
 - [MediaMusicListResponse](docs/MediaMusicListResponse.md)
 - [MediaMusicOperation](docs/MediaMusicOperation.md)
 - [MediaMusicStatus](docs/MediaMusicStatus.md)
 - [MediaMusicStatusResponse](docs/MediaMusicStatusResponse.md)
 - [MotionsInfo](docs/MotionsInfo.md)
 - [MotionsList](docs/MotionsList.md)
 - [MotionsListResponse](docs/MotionsListResponse.md)
 - [MotionsOperation](docs/MotionsOperation.md)
 - [MotionsParameter](docs/MotionsParameter.md)
 - [MotionsStatus](docs/MotionsStatus.md)
 - [MotionsStatusResponse](docs/MotionsStatusResponse.md)
 - [Name](docs/Name.md)
 - [RuntimeResponse](docs/RuntimeResponse.md)
 - [SensorsEnvironmentInfo](docs/SensorsEnvironmentInfo.md)
 - [SensorsEnvironmentValue](docs/SensorsEnvironmentValue.md)
 - [SensorsEnvironmentValueResponse](docs/SensorsEnvironmentValueResponse.md)
 - [SensorsGyroInfo](docs/SensorsGyroInfo.md)
 - [SensorsGyroValue](docs/SensorsGyroValue.md)
 - [SensorsGyroValueResponse](docs/SensorsGyroValueResponse.md)
 - [SensorsInfo](docs/SensorsInfo.md)
 - [SensorsInfraredInfo](docs/SensorsInfraredInfo.md)
 - [SensorsInfraredValue](docs/SensorsInfraredValue.md)
 - [SensorsInfraredValueResponse](docs/SensorsInfraredValueResponse.md)
 - [SensorsList](docs/SensorsList.md)
 - [SensorsListResponse](docs/SensorsListResponse.md)
 - [SensorsOperationRequest](docs/SensorsOperationRequest.md)
 - [SensorsParameter](docs/SensorsParameter.md)
 - [SensorsPressureInfo](docs/SensorsPressureInfo.md)
 - [SensorsPressureValue](docs/SensorsPressureValue.md)
 - [SensorsPressureValueResponse](docs/SensorsPressureValueResponse.md)
 - [SensorsTouchInfo](docs/SensorsTouchInfo.md)
 - [SensorsTouchValue](docs/SensorsTouchValue.md)
 - [SensorsTouchValueResponse](docs/SensorsTouchValueResponse.md)
 - [SensorsUltrasonicInfo](docs/SensorsUltrasonicInfo.md)
 - [SensorsUltrasonicValue](docs/SensorsUltrasonicValue.md)
 - [SensorsUltrasonicValueResponse](docs/SensorsUltrasonicValueResponse.md)
 - [ServosAngles](docs/ServosAngles.md)
 - [ServosAnglesRequest](docs/ServosAnglesRequest.md)
 - [ServosAnglesResponse](docs/ServosAnglesResponse.md)
 - [ServosList](docs/ServosList.md)
 - [ServosMode](docs/ServosMode.md)
 - [ServosModeRequest](docs/ServosModeRequest.md)
 - [ServosModeResponse](docs/ServosModeResponse.md)
 - [ServosResult](docs/ServosResult.md)
 - [ServosResultResponse](docs/ServosResultResponse.md)
 - [SubscriptionsAsrVoice](docs/SubscriptionsAsrVoice.md)
 - [SubscriptionsAsrVoiceDelete](docs/SubscriptionsAsrVoiceDelete.md)
 - [SubscriptionsIatVoice](docs/SubscriptionsIatVoice.md)
 - [SubscriptionsIatVoiceDelete](docs/SubscriptionsIatVoiceDelete.md)
 - [SubscriptionsMotions](docs/SubscriptionsMotions.md)
 - [SubscriptionsMotionsDelete](docs/SubscriptionsMotionsDelete.md)
 - [SubscriptionsSensors](docs/SubscriptionsSensors.md)
 - [SubscriptionsSensorsDelete](docs/SubscriptionsSensorsDelete.md)
 - [SubscriptionsTtsVoice](docs/SubscriptionsTtsVoice.md)
 - [SubscriptionsTtsVoiceDelete](docs/SubscriptionsTtsVoiceDelete.md)
 - [SubscriptionsVisions](docs/SubscriptionsVisions.md)
 - [SubscriptionsVisionsDelete](docs/SubscriptionsVisionsDelete.md)
 - [TotalTime](docs/TotalTime.md)
 - [VisionsAnalysis](docs/VisionsAnalysis.md)
 - [VisionsDeleteTags](docs/VisionsDeleteTags.md)
 - [VisionsGetResponse](docs/VisionsGetResponse.md)
 - [VisionsPhoto](docs/VisionsPhoto.md)
 - [VisionsPhotoListResponse](docs/VisionsPhotoListResponse.md)
 - [VisionsPhotoResponse](docs/VisionsPhotoResponse.md)
 - [VisionsPut](docs/VisionsPut.md)
 - [VisionsPutResponse](docs/VisionsPutResponse.md)
 - [VisionsPutTags](docs/VisionsPutTags.md)
 - [VisionsQuantity](docs/VisionsQuantity.md)
 - [VisionsResults](docs/VisionsResults.md)
 - [VisionsStream](docs/VisionsStream.md)
 - [VisionsTagsResponse](docs/VisionsTagsResponse.md)
 - [VisionsTask](docs/VisionsTask.md)
 - [VoiceAsrOption](docs/VoiceAsrOption.md)
 - [VoiceDeleteOfflineSyntax](docs/VoiceDeleteOfflineSyntax.md)
 - [VoiceGetOfflineSyntaxGrammarsResponse](docs/VoiceGetOfflineSyntaxGrammarsResponse.md)
 - [VoiceGetOfflineSyntaxResponse](docs/VoiceGetOfflineSyntaxResponse.md)
 - [VoiceGetResponse](docs/VoiceGetResponse.md)
 - [VoiceIatRequest](docs/VoiceIatRequest.md)
 - [VoiceOfflineSlot](docs/VoiceOfflineSlot.md)
 - [VoiceOfflineSyntaxRule](docs/VoiceOfflineSyntaxRule.md)
 - [VoicePostOfflineSyntax](docs/VoicePostOfflineSyntax.md)
 - [VoicePutOfflineSyntax](docs/VoicePutOfflineSyntax.md)
 - [VoiceResponse](docs/VoiceResponse.md)
 - [VoiceTTSStr](docs/VoiceTTSStr.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

swenggroup@ubtrobot.com

# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[YanAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 2.7+

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python -m openadk
```

and open your browser to here:

```
http://localhost:10101/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:10101/v1/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t openadk .

# starting up a container
docker run -p 10101:10101 openadk
```
