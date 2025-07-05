```dart
import 'package:flutter/material.dart';
import 'confirmation_page.dart';

class ReportForm extends StatefulWidget {
  @override
  _ReportFormState createState() => _ReportFormState();
}

class _ReportFormState extends State<ReportForm> {
  String _incidentType = 'Human';
  final _locationController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Submit Report')),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            DropdownButton<String>(
              value: _incidentType,
              items: ['Human', 'Animal'].map((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
              onChanged: (newValue) {
                setState(() {
                  _incidentType = newValue!;
                });
              },
            ),
            TextField(
              controller: _locationController,
              decoration: InputDecoration(labelText: 'Location'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text('Submit'),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => ConfirmationPage(
                      incidentType: _incidentType,
                      location: _locationController.text,
                    ),
                  ),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}

import 'package:cloud_firestore/cloud_firestore.dart';

ElevatedButton(
  child: Text('Submit'),
  onPressed: () async {
    await FirebaseFirestore.instance.collection('incidents').add({
      'type': _incidentType,
      'location': _locationController.text,
      'timestamp': DateTime.now().toIso8601String(),
    });

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ConfirmationPage(
          incidentType: _incidentType,
          location: _locationController.text,
        ),
      ),
    );
  },
)
```
