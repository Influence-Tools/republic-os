---
type: Jurisdiction
title: "Butler County, PA"
classification: county
fips: "42019"
state: "PA"
demographics:
  population: 197254
  population_under_18: 37980
  population_18_64: 118579
  population_65_plus: 40695
  median_household_income: 89843
  poverty_rate: 8.15
  homeownership_rate: 76.94
  unemployment_rate: 4.41
  median_home_value: 294200
  gini_index: 0.455
  vacancy_rate: 7.5
  race_white: 183018
  race_black: 2113
  race_asian: 2846
  race_native: 223
  hispanic: 3981
  bachelors_plus: 76890
districts:
  - to: "us/states/pa/districts/16"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/senate/21"
    rel: in-district
    area_weight: 0.8222
  - to: "us/states/pa/districts/senate/47"
    rel: in-district
    area_weight: 0.1777
  - to: "us/states/pa/districts/house/8"
    rel: in-district
    area_weight: 0.3352
  - to: "us/states/pa/districts/house/17"
    rel: in-district
    area_weight: 0.3042
  - to: "us/states/pa/districts/house/11"
    rel: in-district
    area_weight: 0.2697
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Butler County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 197254 |
| Under 18 | 37980 |
| 18–64 | 118579 |
| 65+ | 40695 |
| Median household income | 89843 |
| Poverty rate | 8.15 |
| Homeownership rate | 76.94 |
| Unemployment rate | 4.41 |
| Median home value | 294200 |
| Gini index | 0.455 |
| Vacancy rate | 7.5 |
| White | 183018 |
| Black | 2113 |
| Asian | 2846 |
| Native | 223 |
| Hispanic/Latino | 3981 |
| Bachelor's or higher | 76890 |

## Districts

- [PA-16](/us/states/pa/districts/16.md) — 100% (congressional)
- [PA Senate District 21](/us/states/pa/districts/senate/21.md) — 82% (state senate)
- [PA Senate District 47](/us/states/pa/districts/senate/47.md) — 18% (state senate)
- [PA House District 8](/us/states/pa/districts/house/8.md) — 34% (state house)
- [PA House District 17](/us/states/pa/districts/house/17.md) — 30% (state house)
- [PA House District 11](/us/states/pa/districts/house/11.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
