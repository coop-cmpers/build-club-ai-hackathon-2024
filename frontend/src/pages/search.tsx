import { Button, CircularProgress, Grid, Stack, TextField, Typography } from "@mui/material";
import React, { useState } from "react";
import { SuggestionSection } from "../components/suggestion-section";

const Search = () => {
  const [keyword, setKeyword] = useState("");
  const [location, setLocation] = useState("");
  const [volunteering, setVolunteering] = useState("");
  const [occupations, setOccupations] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const getSuggestions = async () => {
    setVolunteering("");
    setOccupations([]);
    setIsLoading(true);

    const url = `http://${process.env["REACT_APP_BACKEND_HOST"]}:${process.env["REACT_APP_BACKEND_PORT"]}/getrecommendations?location=${location}&keyword=${keyword}`;
    const response = await fetch(url);
    const json = await response.json();

    setVolunteering(json.volunteering);
    setOccupations(json.occupations);
    setIsLoading(false);
  };

  const occupationsToMarkdown = (occupations: string[]) => {
    let markdown = "**If you enjoy these volunteering opportunities, consider these career paths to further your passion:**\n"
    for (const index in occupations) {
      markdown = markdown.concat(`${index + 1}. ${occupations[index]}\n`);
    }
    console.log(markdown)
    return markdown
  };

  return (
    <>
      <Grid
        container
        width="100%"
        height="100%"
        paddingX={15}
        paddingY={5}
        justifyContent="center"
      >
        <Stack alignItems="center">
          <Typography variant="h1">Voluntario</Typography>
          <Typography variant="caption" color="grey" fontStyle="italic">Find out how you can change the world!</Typography>
        </Stack>
        <Grid
          container
          alignItems="center"
          justifyContent="center"
          marginY={4}
        >
          <Stack
            direction="column"
            width="30%"
            spacing={5}
            alignItems="center"
          >
            <TextField
              variant="standard"
              onChange={(e) => setKeyword(e.target.value)}
              placeholder="What's your keyword?"
              fullWidth
            /> 
            <TextField
              variant="standard"
              onChange={(e) => setLocation(e.target.value)}
              placeholder="Where do you want to search in?"
              fullWidth
            />  
            {!isLoading ? (
              <Button onClick={() => getSuggestions()}>Find Volunteering Opportunities!</Button>
            ) : (
              <CircularProgress />
            )}
          </Stack>
        </Grid>
        <Stack direction="column" spacing={5}>
          {volunteering && (
            <SuggestionSection markdown={volunteering} color="#e9edc9"/>
          )}
          {occupations.length !== 0 && (
            <SuggestionSection markdown={occupationsToMarkdown(occupations)} color="#c6eafc" />
          )}
        </Stack>
      </Grid>
      <Stack marginLeft={3} marginBottom={1}>
        <Typography variant="caption" color="grey">Powered by JigsawStack and Google Gemini 💪</Typography>
      </Stack>
    </>
  );
};

export default Search;