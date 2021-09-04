import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:todo/constants/colors.dart';
import 'package:todo/screens/loading/animations.dart';

class LoadingLogo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GetBuilder<LoadingAnimationsController>(builder: (_) {
      return Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          AnimatedOpacity(
            opacity: _.logoOpacity,
            duration: _.animationSpeed,
            child: AnimatedPadding(
              duration: _.animationSpeed,
              padding: _.logoTextpadding,
              child: Icon(Icons.check_circle_outline_rounded,
                  color: kSecondaryColor,
                  size: MediaQuery.of(context).size.width * 0.75),
            ),
          ),
          AnimatedOpacity(
            opacity: _.textOpacity,
            duration: _.animationSpeed,
            child: Text(
              "ToDo app",
              style: GoogleFonts.ubuntu(
                  color: kSecondaryColor,
                  fontWeight: FontWeight.w900,
                  fontSize: 30),
            ),
          )
        ],
      );
    });
  }
}
