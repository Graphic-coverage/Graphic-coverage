import { teamCover } from './teamCover';
import * as fs from 'fs/promises';

let data: teamCover[] = [];

async function load(start: number, end: number) {
    try {
        // Read JSON file
        const jsonData = await fs.readFile('./jsons/teamsCover.json', 'utf8');
        const teams = JSON.parse(jsonData).teams;

        // Iterate through the specified range and insert data into the array
        for (let i = start; i <= end; i++) {
            const teamData = teams[i - 1]; // Adjust index since team numbers start from 1
            const team_cover = new teamCover();

            // Your existing code for populating team_cover...

            data.push(team_cover);
        }

        // Example: Load teams from 1 to 5
        await load(1, 5);

        // Print the result
        console.log(data);
    } catch (error) {
        console.error('Error reading file:', error);
    }
}
