```dart
import 'package:flutter/material.dart';
import 'report_form.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('🚨 RoadAid AI')),
      body: Center(
        child: ElevatedButton(
          child: Text('Report an Incident'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ReportForm()),
            );
          },
        ),
      ),
    );
  }
}
```
