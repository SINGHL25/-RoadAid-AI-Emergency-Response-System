```dart
import 'package:flutter/material.dart';
import 'pages/home_page.dart';

void main() => runApp(RoadAidApp());

class RoadAidApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'RoadAid AI',
      theme: ThemeData(primarySwatch: Colors.red),
      home: HomePage(),
    );
  }
}
```
