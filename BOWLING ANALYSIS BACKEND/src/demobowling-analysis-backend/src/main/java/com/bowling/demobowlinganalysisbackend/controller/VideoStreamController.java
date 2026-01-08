package com.bowling.demobowlinganalysisbackend.controller;

import org.springframework.http.*;
import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

@RestController
@RequestMapping("/video")
public class VideoStreamController {

    private static final String DIR = "D:/bowling_uploads/";

    @GetMapping("/{filename}")
    public ResponseEntity<byte[]> streamVideo(@PathVariable String filename,
                                              @RequestHeader(value = "Range", required = false) String range)
            throws IOException {

        File file = new File(DIR + filename);
        if (!file.exists()) {
            return ResponseEntity.notFound().build();
        }

        long fileLength = file.length();
        byte[] data = Files.readAllBytes(file.toPath());

        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CONTENT_TYPE, "video/mp4");
        headers.set(HttpHeaders.ACCEPT_RANGES, "bytes");
        headers.setContentLength(fileLength);

        return new ResponseEntity<>(data, headers, HttpStatus.PARTIAL_CONTENT);
    }
}
