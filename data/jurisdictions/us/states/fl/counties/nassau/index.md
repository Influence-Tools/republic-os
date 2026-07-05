---
type: Jurisdiction
title: "Nassau County, FL"
classification: county
fips: "12089"
state: "FL"
demographics:
  population: 97859
  population_under_18: 18923
  population_18_64: 55541
  population_65_plus: 23395
  median_household_income: 89804
  poverty_rate: 9.68
  homeownership_rate: 82.72
  unemployment_rate: 4.48
  median_home_value: 382800
  gini_index: 0.4461
  vacancy_rate: 12.76
  race_white: 83225
  race_black: 5447
  race_asian: 1315
  race_native: 256
  hispanic: 5570
  bachelors_plus: 35697
districts:
  - to: "us/states/fl/districts/04"
    rel: in-district
    area_weight: 0.9184
  - to: "us/states/fl/districts/senate/4"
    rel: in-district
    area_weight: 0.9215
  - to: "us/states/fl/districts/house/15"
    rel: in-district
    area_weight: 0.9215
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Nassau County, FL

County jurisdiction — 35 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 97859 |
| Under 18 | 18923 |
| 18–64 | 55541 |
| 65+ | 23395 |
| Median household income | 89804 |
| Poverty rate | 9.68 |
| Homeownership rate | 82.72 |
| Unemployment rate | 4.48 |
| Median home value | 382800 |
| Gini index | 0.4461 |
| Vacancy rate | 12.76 |
| White | 83225 |
| Black | 5447 |
| Asian | 1315 |
| Native | 256 |
| Hispanic/Latino | 5570 |
| Bachelor's or higher | 35697 |

## Districts

- [FL-04](/us/states/fl/districts/04.md) — 92% (congressional)
- [FL Senate District 4](/us/states/fl/districts/senate/4.md) — 92% (state senate)
- [FL House District 15](/us/states/fl/districts/house/15.md) — 92% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
