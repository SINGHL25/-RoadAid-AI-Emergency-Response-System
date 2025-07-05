```dart
import 'package:flutter/material.dart';

class ConfirmationPage extends StatelessWidget {
  final String incidentType;
  final String location;

  ConfirmationPage({required this.incidentType, required this.location});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Confirmation')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.check_circle, color: Colors.green, size: 100),
            Text('Report Submitted!'),
            Text('Type: $incidentType'),
            Text('Location: $location'),
          ],
        ),
      ),
    );
  }
}
```

