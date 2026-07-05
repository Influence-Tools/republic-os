---
type: Jurisdiction
title: "Mackinac County, MI"
classification: county
fips: "26097"
state: "MI"
demographics:
  population: 10957
  population_under_18: 1641
  population_18_64: 6061
  population_65_plus: 3255
  median_household_income: 63909
  poverty_rate: 16.05
  homeownership_rate: 77.88
  unemployment_rate: 7.97
  median_home_value: 174500
  gini_index: 0.4472
  vacancy_rate: 50.94
  race_white: 7852
  race_black: 525
  race_asian: 67
  race_native: 1502
  hispanic: 247
  bachelors_plus: 2978
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.5199
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.2672
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.2451
  - to: "us/states/mi/districts/house/107"
    rel: in-district
    area_weight: 0.2672
  - to: "us/states/mi/districts/house/108"
    rel: in-district
    area_weight: 0.2452
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Mackinac County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10957 |
| Under 18 | 1641 |
| 18–64 | 6061 |
| 65+ | 3255 |
| Median household income | 63909 |
| Poverty rate | 16.05 |
| Homeownership rate | 77.88 |
| Unemployment rate | 7.97 |
| Median home value | 174500 |
| Gini index | 0.4472 |
| Vacancy rate | 50.94 |
| White | 7852 |
| Black | 525 |
| Asian | 67 |
| Native | 1502 |
| Hispanic/Latino | 247 |
| Bachelor's or higher | 2978 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 52% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 27% (state senate)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 25% (state senate)
- [MI House District 107](/us/states/mi/districts/house/107.md) — 27% (state house)
- [MI House District 108](/us/states/mi/districts/house/108.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
