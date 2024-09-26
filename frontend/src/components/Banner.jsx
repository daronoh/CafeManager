import React from 'react';
import { Box, Typography } from '@mui/material';

const Banner = () => {
    return (
        <Box 
            sx={{
                backgroundColor: '#3f51b5',
                color: 'white',
                padding: '20px',
                textAlign: 'center',
                boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
                marginBottom: '20px'
            }}
        >
            <Typography variant="h4">Cafe Manager!</Typography>
            <Typography variant="subtitle1">Manage your cafes with ease.</Typography>
        </Box>
    );
};

export default Banner;