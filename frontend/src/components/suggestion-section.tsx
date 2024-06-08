import { Box } from "@mui/material";
import MuiMarkdown from "mui-markdown";
import React from "react";

interface SuggestionSectionProps {
  markdown: string;
  color: string;
}

export const SuggestionSection = ({ markdown, color }: SuggestionSectionProps) => {
  return (
    <Box
      sx={{ borderRadius: "1%" }}
      bgcolor={color}
      padding={10}
      color="#495057"
      width="100%"
    >
      <MuiMarkdown>{markdown}</MuiMarkdown>
    </Box>
  );
}