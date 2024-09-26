import React from 'react';
import { Link } from '@tanstack/react-router';

const HomePage = () => {
    const styles = {
        homepage: {
            textAlign: 'center',
            padding: '50px',
            backgroundColor: '#f9f9f9',
            minHeight: '100vh',
        },
        heading: {
            fontSize: '2.5em',
            marginBottom: '30px',
            color: '#333',
        },
        buttonContainer: {
            display: 'flex',
            justifyContent: 'center',
            gap: '20px',
        },
        button: {
            padding: '15px 25px',
            fontSize: '1.2em',
            color: 'white',
            backgroundColor: '#007bff',
            border: 'none',
            borderRadius: '5px',
            textDecoration: 'none',
            transition: 'background-color 0.3s',
        },
        buttonHover: {
            backgroundColor: '#0056b3',
        },
    };

    return (
        <div style={styles.homepage}>
            <h1 style={styles.heading}>Welcome!</h1>
            <div style={styles.buttonContainer}>
                <Link to="/cafes" style={styles.button}>Go to Cafes</Link>
                <Link to="/employees" style={styles.button}>Go to Employees</Link>
            </div>
        </div>
    );
};

export default HomePage;