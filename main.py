import telebot
import requests
import json,time
from urllib.parse import quote

API_TOKEN = 'هنا توكن البوت الخاص بك'
bot = telebot.TeleBot(API_TOKEN)

def insta_login(message,username,password):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Instagram 339.0.0.0.81 Android (34/14; 532dpi; 1440x2969; samsung; SM-S928B; e3q; qcom; ar_AE; 618388982)',    'x-ig-app-locale': 'ar_AE',    'x-ig-device-locale': 'ar_AE',    'x-ig-mapped-locale': 'ar_AR',    'x-pigeon-session-id': 'UFS-9bc8cf8b-87e4-4fd7-bec1-ccabccf68303-0',    'x-pigeon-rawclienttime': '1720831235.107',    'x-ig-bandwidth-speed-kbps': '-1.000',    'x-ig-bandwidth-totalbytes-b': '0',    'x-ig-bandwidth-totaltime-ms': '0',    'x-bloks-version-id': '447ea0d1407a78f1b163144331b28c072fdc368581d74667a89052898d4a9bcf',    'x-ig-www-claim': '0',    'x-bloks-is-prism-enabled': 'false',    'x-bloks-prism-button-version': 'CONTROL',    'x-bloks-prism-colors-enabled': 'false',    'x-bloks-prism-font-enabled': 'false',    'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[0],"challenge_nonce":"VXY0nLpKOQCMJlxv1EkcaNodwgbI9FZG","signed_nonce":"MEUCIDm3v29LQobyuMl-LlBaTbKBgweGCOAyAF8cfTukT5KLAiEA03ryj6mPPaCfY-Fl7mVNeAr62BCcSnUGr_EqBBsoZfI=","key_hash":"ba64caf06b9f846d18a162565bdd6e502402bec32bb1b7dc55320de7ec727629","certificate_chain":"-----BEGIN CERTIFICATE-----\\nMIICnjCCAkWgAwIBAgIBATAKBggqhkjOPQQDAjAvMRkwFwYDVQQFExBmNjY2YmFiYTg0M2RhYWQ3\\nMRIwEAYDVQQMDAlTdHJvbmdCb3gwHhcNMjQwNzEzMDA0MDE2WhcNMzQwNzEzMDA0MDE2WjAfMR0w\\nGwYDVQQDExRBbmRyb2lkIEtleXN0b3JlIEtleTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABP0T\\nFuMRSXqc1v\\/e2bI9kvj9RYZ\\/BwFQdsmPAGGn4M9nrJ\\/rtAKyUioH5ZJDtUh7cO3vlcpIdlNSuzxP\\nTnvbUuyjggFgMIIBXDAOBgNVHQ8BAf8EBAMCB4AwggFIBgorBgEEAdZ5AgERBIIBODCCATQCAgEs\\nCgECAgIBLAoBAgQgaXpJQ3VrbDRFVDZhMWR4R01tcVBlaEtnV1hzakJEUXcEADBZv4U9CAIGAZCp\\niIy5v4VFSQRHMEUxHzAdBBVjb20uaW5zdGFncmFtLmFuZHJvaWQCBBZJXLoxIgQgpA2oClnRcMqp\\nUM8VwYxFTUejmyaYnYtkDs10W6cb9dwwgaShCDEGAgECAgEDogMCAQOjBAICAQClBTEDAgEEqgMC\\nAQG\\/g3cCBQC\\/hT4DAgEAv4VATDBKBCAV9mmQsythNQj6mXml\\/HCqN8s8PWBD6CqZh2VxbW9avQEB\\n\\/woBAAQgXTNcmCpFzl0mcRdnfGybxlBDHwGykXLkCQP42stvmaq\\/hUEFAgMCIuC\\/hUIFAgMDFqa\\/\\nhU4GAgQBNNjZv4VPBgIEATTY2TAKBggqhkjOPQQDAgNHADBEAiB\\/ZNii4zNNavs7lcGX\\/orwy9Eb\\ntghHF5EEKsCgctwqsQIgJSrMjYB0E1jpzbbjDJkfZvTgvF5b6Xuj42uolRzE06M=\\n-----END CERTIFICATE-----\\n-----BEGIN CERTIFICATE-----\\nMIICMTCCAbegAwIBAgIKFmgwIwaFORJXlzAKBggqhkjOPQQDAjAvMRkwFwYDVQQFExA1YmE4ODMw\\nOTc0ZjI1ZWNiMRIwEAYDVQQMDAlTdHJvbmdCb3gwHhcNMjIwNTI1MjA1OTA4WhcNMzIwNTIyMjA1\\nOTA4WjAvMRkwFwYDVQQFExBmNjY2YmFiYTg0M2RhYWQ3MRIwEAYDVQQMDAlTdHJvbmdCb3gwWTAT\\nBgcqhkjOPQIBBggqhkjOPQMBBwNCAATLxPGqbxreTXguw8+HyLFy42f4JXVSqTYui++gyrtHxb8A\\nya\\/wUTUmxIMXQ9s9nM3BPOJYvi096OWebhi3BGJio4G6MIG3MB0GA1UdDgQWBBTpzHVmSOmfV0RB\\njDb8Piaw4y7nfjAfBgNVHSMEGDAWgBRR0OQJyewFWOHjN6znnCP\\/dI5sazAPBgNVHRMBAf8EBTAD\\nAQH\\/MA4GA1UdDwEB\\/wQEAwICBDBUBgNVHR8ETTBLMEmgR6BFhkNodHRwczovL2FuZHJvaWQuZ29v\\nZ2xlYXBpcy5jb20vYXR0ZXN0YXRpb24vY3JsLzE2NjgzMDIzMDY4NTM5MTI1Nzk3MAoGCCqGSM49\\nBAMCA2gAMGUCMDukjFM56Z1norB59dM2Q85P4YWVS2rV7gRAhFUSmJVpBAV5YeV1Vd+w1yHhkjyp\\nVQIxAI0qB3SU\\/pyP1itJhPx3C7Oy6Vke5lDilhzcLZVSuHb4b7KUmLEA\\/N4okWcp8Fc1zg==\\n-----END CERTIFICATE-----\\n-----BEGIN CERTIFICATE-----\\nMIID1zCCAb+gAwIBAgIKA4gmZ2BliZaGEDANBgkqhkiG9w0BAQsFADAbMRkwFwYDVQQFExBmOTIw\\nMDllODUzYjZiMDQ1MB4XDTIyMDUyNTIwMzYzOFoXDTMyMDUyMjIwMzYzOFowLzEZMBcGA1UEBRMQ\\nNWJhODgzMDk3NGYyNWVjYjESMBAGA1UEDAwJU3Ryb25nQm94MHYwEAYHKoZIzj0CAQYFK4EEACID\\nYgAEEsealjrEYkY\\/ngNBAsIwXrrLYjHEzYFvT9dU8aFvZWzOG4xa3uQJWPcFPY1HoYpI+KzBm4Yz\\nUbt4zYeGNjoov1E8wHA2wg\\/S4rmITsFAu8X62UltptbREuOGP6p8\\/Vb4o4G2MIGzMB0GA1UdDgQW\\nBBRR0OQJyewFWOHjN6znnCP\\/dI5sazAfBgNVHSMEGDAWgBQ2YeEAfIgFCVGLRGxH\\/xpMyepPEjAP\\nBgNVHRMBAf8EBTADAQH\\/MA4GA1UdDwEB\\/wQEAwICBDBQBgNVHR8ESTBHMEWgQ6BBhj9odHRwczov\\nL2FuZHJvaWQuZ29vZ2xlYXBpcy5jb20vYXR0ZXN0YXRpb24vY3JsL0YxQzE3MkE2OTlFQUY1MUQw\\nDQYJKoZIhvcNAQELBQADggIBAHrprDsAXE9VuxyMFjM+r+veMplhocS09y\\/rTgm9\\/SYnaQuvfan6\\n1dmP02VEVDG2+Ku0KRd\\/IdlbByRaxlD1an6vsCnUMbR0gG+ndEc7eE0V5TMjDkP4tEUbTwauvzbm\\nTN2HsFnmBfa+Bd9vhzfjs3nryZDFc1n9ijmIpX\\/mzBAnRuBRyg6M69BxJ4zOMdxInHdu1MLfmRg7\\n02lJy5skTjpmMervRMHuj3AwFmuP4D8ZEiXejn\\/NDQWKRd+gTZwTMrj\\/KHbLcKwNOvxaVNSTxdL4\\nJ4qzaG\\/HCKKw8tsxk5QfAfGFE2t32dlxWdWgA1xXUInpUtOWy6IkpbhldSw4m22kZVMSKr8ba4U2\\nNj7bAeb1ypiOEU7DI\\/CEiynd9cOdYS8GG2LQnvNCU25HsaBV0ShaAUumvriDgN5UEZVnZ4HyhSXj\\nfwWpfCrBq46hzq0NPHFBNVRkBpqN5QDZJpNKCUJxOp\\/wWqFe518hb4B1cwXdZ2O4Dv3vIiHyEv2x\\nUsQsskB22ytir4t1RXKAnazCwcsY3FY9LK3Rl9iNcJSmbMcFstDxg0LK6OgDHlHNCaP5GWyaS9E2\\nRnT8j6GwxIU13eG0iDHzZZyqVt7t0FYJ5aLSv+TagMoKn4sh+VGbO+4d7DtkQoQHCkJnWlr76YQe\\nHycV6GgUF\\/nR1stcobsyb3hY\\n-----END CERTIFICATE-----\\n-----BEGIN CERTIFICATE-----\\nMIIFHDCCAwSgAwIBAgIJAPHBcqaZ6vUdMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNVBAUTEGY5MjAw\\nOWU4NTNiNmIwNDUwHhcNMjIwMzIwMTgwNzQ4WhcNNDIwMzE1MTgwNzQ4WjAbMRkwFwYDVQQFExBm\\nOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHs\\nK7Qui8xUFmOr75gvMsd\\/dTEDDJdSSxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfd\\nnJLmN0pTy\\/4lj4\\/7tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y\\/\\/0rb+T+W8a9nsNL\\n\\/ggjnar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB\\/M0n1n\\/W9nGqC4FSYa04\\nT6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl\\/m00QLVWutHQoVJYnFPlXTcHYvASLu+R\\nhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+OJtvsBslHZvPBKCOdT0MS+tgSOIfga+z1\\nZ1g7+DVagf7quvmag8jfPioyKvxnK\\/EgsTUVi2ghzq8wm27ud\\/mIM7AY2qEORR8Go3TVB4HzWQgp\\nZrt3i5MIlCaY504LzSRiigHCzAPlHws+W0rB5N+er5\\/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6\\ntUXHI\\/+MRPjy02i59lINMRRev56GKtcd9qO\\/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9EaDK8\\nZ4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR\\/bkwSWc+NpUFgNPN9PvQi8WEg5UmAGMCAwEAAaNjMGEw\\nHQYDVR0OBBYEFDZh4QB8iAUJUYtEbEf\\/GkzJ6k8SMB8GA1UdIwQYMBaAFDZh4QB8iAUJUYtEbEf\\/\\nGkzJ6k8SMA8GA1UdEwEB\\/wQFMAMBAf8wDgYDVR0PAQH\\/BAQDAgIEMA0GCSqGSIb3DQEBCwUAA4IC\\nAQB8cMqTllHc8U+qCrOlg3H7174lmaCsbo\\/bJ0C17JEgMLb4kvrqsXZs01U3mB\\/qABg\\/1t5Pd5AO\\nRHARs1hhqGICW\\/nKMav574f9rZN4PC2ZlufGXb7sIdJpGiO9ctRhiLuYuly10JccUZGEHpHSYM2G\\ntkgYbZba6lsCPYAAP83cyDV+1aOkTf1RCp\\/lM0PKvmxYN10RYsK631jrleGdcdkxoSK\\/\\/mSQbgcW\\nnmAEZrzHoF1\\/0gso1HZgIn0YLzVhLSA\\/iXCX4QT2h3J5z3znluKG1nv8NQdxei2DIIhASWfu804C\\nA96cQKTTlaae2fweqXjdN1\\/v2nqOhngNyz1361mFmr4XmaKH\\/ItTwOe72NI9ZcwS1lVaCvsIkTDC\\nEXdm9rCNPAY10iTunIHFXRh+7KPzlHGewCq\\/8TOohBRn0\\/NNfh7uRslOSZ\\/xKbN9tMBtw37Z8d2v\\nvnXq\\/YWdsm1+JLVwn6yYD\\/yacNJBlwpddla8eaVMjsF6nBnIgQOf9zKSe06nSTqvgwUHosgOECZJ\\nZ1EuzbH4yswbt02tKtKEFhx+v+OTge\\/06V+jGsqTWLsfrOCNLuA8H++z+pUENmpqnnHovaI47gC+\\nTNpkgYGkkBT6B\\/m\\/U01BuOBBTzhIlMEZq9qkDWuM2cA5kW5V3FJUcfHnw1IdYIg2Wxg7yHcQZemF\\nQg==\\n-----END CERTIFICATE-----"}]}',    'x-bloks-is-layout-rtl': 'true',    'x-ig-device-id': '3f284cc1-4663-4451-8fa0-206949935a62',    'x-ig-family-device-id': '412379ba-ca98-4148-8373-131ba4628414',    'x-ig-android-id': 'android-d734f4604840e801',    'x-ig-timezone-offset': '10800',    'x-ig-nav-chain': 'com.bloks.www.caa.login.aymh_single_profile_screen_entry:com.bloks.www.caa.login.aymh_single_profile_screen_entry:1:button:1720831215.857::',    'x-fb-connection-type': 'WIFI',    'x-ig-connection-type': 'WIFI',    'x-ig-capabilities': '3brTv10=',    'x-ig-app-id': '567067343352427',    'priority': 'u=3',    'accept-language': 'ar-AE, en-US',    'x-mid': 'ZpHM7wABAAHM4xyXeTDZ_e75RTNg',    'ig-intended-user-id': '0',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'x-fb-http-engine': 'Liger',    'x-fb-client-ip': 'True',    'x-fb-server-cluster': 'True',})
    data = {'params': '{"client_input_params":{"should_show_nested_nta_from_aymh":1,"device_id":"android-d734f4604840e801","login_attempt_count":1,"secure_family_device_id":"","machine_id":"ZpHM7wABAAHM4xyXeTDZ_e75RTNg","accounts_list":[{"uid":"100067389895254","credential_type":"messenger_active_session","account_type":"","token":"EAADo1TDZCuu8BO6vATf6vH0nfTEXG8oeYt7Cm1fcEZCnlET9NFqIA1PfqabRiZA3RXJZCcTpeIbl4aOSZAeQn792WWtnFhY4EbFkz89HZCBr9a36EreT7CD1xvZABFXwCneQFkMbycGnZC7TZCmlXOZAQP4eRFop9i67Q4ajQkNOw222X9TmzbXsbhy1TRLZBJCkPSWPAZDZD"},{"uid":"100067389895254","credential_type":"messenger_local_auth","account_type":"","token":"EAADo1TDZCuu8BO6vATf6vH0nfTEXG8oeYt7Cm1fcEZCnlET9NFqIA1PfqabRiZA3RXJZCcTpeIbl4aOSZAeQn792WWtnFhY4EbFkz89HZCBr9a36EreT7CD1xvZABFXwCneQFkMbycGnZC7TZCmlXOZAQP4eRFop9i67Q4ajQkNOw222X9TmzbXsbhy1TRLZBJCkPSWPAZDZD"}],"auth_secure_device_id":"","has_whatsapp_installed":1,"password":"#PWD_INSTAGRAM:0:1720831235:'+password+'","sso_token_map_json_string":"{\\"40528646410\\":[{\\"credential_type\\":\\"messenger_active_session\\",\\"token\\":\\"EAADo1TDZCuu8BO6vATf6vH0nfTEXG8oeYt7Cm1fcEZCnlET9NFqIA1PfqabRiZA3RXJZCcTpeIbl4aOSZAeQn792WWtnFhY4EbFkz89HZCBr9a36EreT7CD1xvZABFXwCneQFkMbycGnZC7TZCmlXOZAQP4eRFop9i67Q4ajQkNOw222X9TmzbXsbhy1TRLZBJCkPSWPAZDZD\\"}]}","family_device_id":"412379ba-ca98-4148-8373-131ba4628414","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":"","lara_override":""},"event_flow":"login_manual","event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"client_known_key_hash":"","contact_point":"'+username+'","encrypted_msisdn":""},"server_params":{"should_trigger_override_login_2fa_action":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":"59bbdcf4-876b-4052-8d76-21eeece81136","login_source":"Login","is_platform_login":0,"INTERNAL__latency_qpl_marker_id":36707139,"offline_experiment_group":"caa_iteration_v3_perf_ig_4","is_from_landing_page":0,"password_text_input_id":"eh5lwt:122","is_from_empty_password":0,"ar_event_source":"login_home_page","qe_device_id":"3f284cc1-4663-4451-8fa0-206949935a62","username_text_input_id":"eh5lwt:121","layered_homepage_experiment_group":null,"device_id":"android-d734f4604840e801","INTERNAL__latency_qpl_instance_id":8.7534161300392E13,"reg_flow_source":"aymh_single_profile_native_integration_point","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":null,"INTERNAL_INFRA_THEME":"harm_f","access_flow_version":"F2_FLOW","is_from_logged_in_switcher":0}}',    'bk_client_context': '{"bloks_version":"447ea0d1407a78f1b163144331b28c072fdc368581d74667a89052898d4a9bcf","styles_id":"instagram"}',    'bloks_versioning_id': '447ea0d1407a78f1b163144331b28c072fdc368581d74667a89052898d4a9bcf',}
    response = session.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',  data=data,)
    try:
        data = response.json()["layout"]['bloks_payload']["tree"]
        authorization = data['㐟']['#'].split("Bearer ")[1].split("\\")[0]
        bot.send_message(message.chat.id, f"تم تخزين الجلسة بنجاح")
        session_file = str(message.chat.id)+"_session.txt"
        with open(session_file, 'w') as f:
            f.write(f"{authorization}\n")
        bot.send_message(message.chat.id, f"تم تخزين الجلسة بنجاح ✅️\nاستخدم الامر /run لبدأ التفاعل")
    except:
        bot.send_message(message.chat.id, f"خطأ في تسجيل الدخول تأكد من توثيق الجلسة من تطبيق الانستقرام والموافقه على عملية تسجيلال الدخول ❌️")   

def run_cooments(message,comment):
        session_file = str(message.chat.id)+"_session.txt"
        session = requests.Session()
        authorization = open(session_file, 'r').readline().strip()
        url = "https://b.i.instagram.com/api/v1/multiple_accounts/get_account_family/"
        headers = {  'User-Agent': "Instagram 339.0.0.0.81 Android (34/14; 532dpi; 1440x2969; samsung; SM-S928B; e3q; qcom; ar_AE; 618388982)",  'authorization': f"Bearer {authorization}",}
        response = session.get(url, headers=headers)
        info = response.json()["current_account"]
        name = info["full_name"]
        user_ig = info["username"]
        user_id = info["pk"]
        image = info["profile_pic_url"]
        msg = f"""
STARTING ✅️ BY @ZZIQZ
++++++INFO++++++
USERNAME: {user_ig}
USER_ID: {user_id}
FULL NAME: {name}
+++++STATUS+++++
        """
        lool = bot.send_photo(message.chat.id,photo=image,caption=msg)
        url = "https://i.instagram.com/graphql/query"
        payload ={  "method": "post",  "pretty": False,  "format": "json",  "server_timestamps": True,  "locale": "user",  "fb_api_req_friendly_name": "FollowingList",  "client_doc_id": "16104639283947325226270828876",  "enable_canonical_naming": True,  "enable_canonical_variable_overrides": True,  "enable_canonical_naming_ambiguous_type_prefixing": True,  "variables": {    "include_unseen_count": False,    "enable_groups": True,    "user_id": user_id,    "request_data": {      "search_surface": "follow_list_page",      "rank_token": "c329122f-4b92-4ccd-9630-319a3aca63f2",      "includes_hashtags": True    },    "query": "",    "include_biography": False,    "exclude_unused_fields": False  }}
        headers = {'User-Agent': "Instagram 339.0.0.0.81 Android (34/14; 532dpi; 1440x2969; samsung; SM-S928B; e3q; qcom; ar_AE; 618388982)",'Content-Type': "application/json",'x-fb-friendly-name': "FollowingList",'authorization': f"Bearer {authorization}",'Cookie': "csrftoken=FoAVFdB6itX8gblFqG8S9yI9ONKPPCGg"}
        response = session.post(url, json=payload, headers=headers)
        data_following = response.json()["data"]["1$xdt_api__v1__friendships__following(_request_data:$request_data,enable_groups:$enable_groups,include_friendship_status:true,max_id:$max_id,order:$order,query:$query,user_id:$user_id)"]["users"]
        tta = 0
        for target in data_following:
              tta+=1
              target_id = target["pk"]
              target_user = target["username"]
              msg =f"\nTARGET {tta}\nTARGET USER: {target_user}\n+++++++++++++"
              url = f"https://i.instagram.com/api/v1/feed/user/{target_id}/"
              params = {'exclude_comment': "true",'should_delay_media_metadata_fetch': "false"}
              response = session.get(url, params=params, headers=headers)
              try:
                            first_post = response.json()["items"][0]["id"]
                            headers = {'User-Agent': "Instagram 339.0.0.0.81 Android (34/14; 532dpi; 1440x2969; samsung; SM-S928B; e3q; qcom; ar_AE; 618388982)",'Content-Type': "application/x-www-form-urlencoded ;UTF-8",'x-fb-friendly-name': "FollowingList",'authorization': f"Bearer {authorization}",'Cookie': "csrftoken=FoAVFdB6itX8gblFqG8S9yI9ONKPPCGg"}
                            url = f"https://i.instagram.com/api/v1/media/{first_post}/comment/"
                            payload = f"signed_body=SIGNATURE.%7B%22include_media_code%22%3A%22true%22%2C%22user_breadcrumb%22%3A%22dS0FXfV%2F7fe27cnnvK1ygwdj3CtaSOuqwNcC1HiGTls%3D%5CnNiAyODEzIDAgMTcyMzc1NDU4NjM0OQ%3D%3D%5Cn%22%2C%22starting_clips_media_id%22%3A%22null%22%2C%22comment_creation_key%22%3A%223760a7ed-7a98-492e-afef-ae044b1f1deb%22%2C%22delivery_class%22%3A%22organic%22%2C%22idempotence_token%22%3A%223760a7ed-7a98-492e-afef-ae044b1f1deb%22%2C%22carousel_child_mentions%22%3A%22%5B%5D%22%2C%22include_e2ee_mentioned_user_list%22%3A%22true%22%2C%22include_carousel_child_mentions%22%3A%22false%22%2C%22is_from_carousel_child_thread%22%3A%22false%22%2C%22carousel_index%22%3A%22-1%22%2C%22radio_type%22%3A%22wifi-none%22%2C%22_uid%22%3A%2268066789651%22%2C%22_uuid%22%3A%220207d3d8-c663-4bd2-bece-5add94f8c795%22%2C%22nav_chain%22%3A%22SelfFragment%3Aself_profile%3A3%3Amain_profile%3A1723754549.674%3A%3A%2CFollowListFragment%3Aself_following%3A4%3Abutton%3A1723754572.63%3A%3A%2CUserDetailFragment%3Aprofile%3A5%3Abutton%3A1723754577.807%3A%3A%2CProfileMediaTabFragment%3Aprofile%3A6%3Abutton%3A1723754579.75%3A%3A%2CContextualFeedFragment%3Afeed_contextual%3A7%3Abutton%3A1723754580.312%3A%3A%2CCommentListBottomsheetFragment%3Acomments_v2%3A8%3Abutton%3A1723754581.325%3A%3A%22%2C%22comment_text%22%3A%22{comment}%22%2C%22recs_ix%22%3A%22-1%22%2C%22is_carousel_bumped_post%22%3A%22false%22%2C%22container_module%22%3A%22comments_v2_feed_contextual_profile%22%2C%22feed_position%22%3A%220%22%7D"
                            response = session.post(url, data=payload, headers=headers)
                            bot.edit_message_caption(chat_id=message.chat.id, message_id=lool.message_id,caption=msg)
              except:
                            msg =f"\nTARGET {tta}\nTARGET USER: {target_user}\nليس لديه منشور\n+++++++++++++"
                            bot.edit_message_caption(chat_id=message.chat.id, message_id=lool.message_id,caption=msg)
              time.sleep(120)
        msg = f"\nتم ارسال جميع التعليقات البالغه {tta}\n+++++++++++++"
        bot.edit_message_caption(chat_id=message.chat.id, message_id=lool.message_id,caption=msg)
        
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "مرحبا بك في بوت التفاعل اولا يجب عليك تسجيل الدخول\nمن خلال ارسال الامر /login \nوبعد ذلك يمكنك استخدام الامر /run للبدأ بعملية التفاعل\nمطور البوت @ZZIQZ")


@bot.message_handler(commands=['login'])
def login(message):
    bot.send_message(message.chat.id, "أدخل أسم المستخدم او الايميل أو رقم الهاتف لحسابك الانستقرام:")
    bot.register_next_step_handler(message, get_username)


@bot.message_handler(commands=['run'])
def run(message):
    bot.send_message(message.chat.id, "اكتب التعليق الذي تريد التفاعل به علما سيتم نشر هذا التعليق لكل مستخدم تمت متابعته من حسابك الشخصي")
    bot.register_next_step_handler(message, add_comment)

def add_comment(message):
    comment = quote(message.text)
    run_cooments(message,comment)
    


def get_username(message):
    username = message.text
    bot.send_message(message.chat.id, "أدخل كلمة السر")
    bot.register_next_step_handler(message, get_password, username)

def get_password(message, username):
        password = message.text
        insta_login(message,username,password)



def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            import time 
            time.sleep(15)

if __name__ == "__main__":
    main()




