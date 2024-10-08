// File generated by FlutterFire CLI.
// ignore_for_file: type=lint
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      throw UnsupportedError(
        'DefaultFirebaseOptions have not been configured for web - '
        'you can reconfigure this by running the FlutterFire CLI again.',
      );
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for macos - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.windows:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for windows - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyAOpiR30MTMzvqMdQRKGHAWdL3-6I7dqvA',
    appId: '1:644793377175:android:a81ec68d9e164ce8ae64d2',
    messagingSenderId: '644793377175',
    projectId: 'v-chat-8628e',
    storageBucket: 'v-chat-8628e.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyDXSJtRjKh9NNlpvad0HtUWKHsB4tJRiXM',
    appId: '1:644793377175:ios:934d294205e67559ae64d2',
    messagingSenderId: '644793377175',
    projectId: 'v-chat-8628e',
    storageBucket: 'v-chat-8628e.appspot.com',
    androidClientId: '644793377175-a8se9p98o3lnjd36ksjrglgfpnomfuh4.apps.googleusercontent.com',
    iosClientId: '644793377175-0t3shtoe47sto4s7h8vp71k1s1u95vca.apps.googleusercontent.com',
    iosBundleId: 'com.example.vChat',
  );

}

