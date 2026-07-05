---
type: Jurisdiction
title: "Kalamazoo County, MI"
classification: county
fips: "26077"
state: "MI"
demographics:
  population: 262375
  population_under_18: 55906
  population_18_64: 164129
  population_65_plus: 42340
  median_household_income: 72532
  poverty_rate: 12.66
  homeownership_rate: 64.52
  unemployment_rate: 5.51
  median_home_value: 241800
  gini_index: 0.4734
  vacancy_rate: 6.79
  race_white: 199261
  race_black: 28850
  race_asian: 7470
  race_native: 954
  hispanic: 15483
  bachelors_plus: 96419
districts:
  - to: "us/states/mi/districts/04"
    rel: in-district
    area_weight: 0.7509
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.2491
  - to: "us/states/mi/districts/senate/19"
    rel: in-district
    area_weight: 0.8754
  - to: "us/states/mi/districts/senate/18"
    rel: in-district
    area_weight: 0.1246
  - to: "us/states/mi/districts/house/42"
    rel: in-district
    area_weight: 0.5836
  - to: "us/states/mi/districts/house/45"
    rel: in-district
    area_weight: 0.1858
  - to: "us/states/mi/districts/house/40"
    rel: in-district
    area_weight: 0.1735
  - to: "us/states/mi/districts/house/41"
    rel: in-district
    area_weight: 0.0571
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Kalamazoo County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 262375 |
| Under 18 | 55906 |
| 18–64 | 164129 |
| 65+ | 42340 |
| Median household income | 72532 |
| Poverty rate | 12.66 |
| Homeownership rate | 64.52 |
| Unemployment rate | 5.51 |
| Median home value | 241800 |
| Gini index | 0.4734 |
| Vacancy rate | 6.79 |
| White | 199261 |
| Black | 28850 |
| Asian | 7470 |
| Native | 954 |
| Hispanic/Latino | 15483 |
| Bachelor's or higher | 96419 |

## Districts

- [MI-04](/us/states/mi/districts/04.md) — 75% (congressional)
- [MI-05](/us/states/mi/districts/05.md) — 25% (congressional)
- [MI Senate District 19](/us/states/mi/districts/senate/19.md) — 88% (state senate)
- [MI Senate District 18](/us/states/mi/districts/senate/18.md) — 12% (state senate)
- [MI House District 42](/us/states/mi/districts/house/42.md) — 58% (state house)
- [MI House District 45](/us/states/mi/districts/house/45.md) — 19% (state house)
- [MI House District 40](/us/states/mi/districts/house/40.md) — 17% (state house)
- [MI House District 41](/us/states/mi/districts/house/41.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
