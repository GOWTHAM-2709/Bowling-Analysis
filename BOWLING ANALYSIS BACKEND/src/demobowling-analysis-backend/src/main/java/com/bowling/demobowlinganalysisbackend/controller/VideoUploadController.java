package com.bowling.demobowlinganalysisbackend.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;
import java.nio.charset.StandardCharsets;

@RestController
@RequestMapping("/api/video")
public class VideoUploadController {

    private static final String DIR = "D:/bowling_uploads/";

    @PostMapping("/upload")
    public ResponseEntity<String> upload(@RequestParam("file") MultipartFile file) {
        try {
            new File(DIR).mkdirs();
            File saved = new File(DIR + file.getOriginalFilename());
            file.transferTo(saved);

            Process p = Runtime.getRuntime().exec(
                "python src/main/resources/analysis/analysis.py \"" + saved.getAbsolutePath() + "\""
            );

            BufferedReader reader = new BufferedReader(
                new InputStreamReader(p.getInputStream(), StandardCharsets.UTF_8)
            );

            StringBuilder json = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                json.append(line);
            }

            p.waitFor();
            return ResponseEntity.ok(json.toString());

        } catch (Exception e) {
            return ResponseEntity.internalServerError()
                    .body("{\"error\":\""+e.getMessage()+"\"}");
        }
    }
}
