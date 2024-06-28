import 'package:client/core/theme/app_pallete.dart';
import 'package:flutter/material.dart';

class AuthGradientButton extends StatelessWidget {
  final VoidCallback onTap;
  final String action;
  AuthGradientButton({super.key, required this.action,
    required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        borderRadius: BorderRadius.all(Radius.circular(10)),
        gradient: LinearGradient(
          colors: [
            Pallete.gradient1,
            Pallete.gradient2,
          ],
        ),
      ),
      child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.transparent,
            shadowColor: Colors.transparent,
            fixedSize: const Size(395, 55)),
          onPressed: onTap,
          child: Text(
            action,
            style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w600,
            color: Colors.white),
          )),
    );
  }
}
