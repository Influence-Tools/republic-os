---
type: Jurisdiction
title: "Dauphin County, PA"
classification: county
fips: "42043"
state: "PA"
demographics:
  population: 289593
  population_under_18: 64718
  population_18_64: 172654
  population_65_plus: 52221
  median_household_income: 76242
  poverty_rate: 12.87
  homeownership_rate: 63.08
  unemployment_rate: 4.51
  median_home_value: 236400
  gini_index: 0.4611
  vacancy_rate: 5.06
  race_white: 182570
  race_black: 49862
  race_asian: 18938
  race_native: 832
  hispanic: 34032
  bachelors_plus: 95020
districts:
  - to: "us/states/pa/districts/10"
    rel: in-district
    area_weight: 0.9956
  - to: "us/states/pa/districts/senate/15"
    rel: in-district
    area_weight: 0.5334
  - to: "us/states/pa/districts/senate/34"
    rel: in-district
    area_weight: 0.4664
  - to: "us/states/pa/districts/house/125"
    rel: in-district
    area_weight: 0.6408
  - to: "us/states/pa/districts/house/106"
    rel: in-district
    area_weight: 0.2427
  - to: "us/states/pa/districts/house/105"
    rel: in-district
    area_weight: 0.052
  - to: "us/states/pa/districts/house/104"
    rel: in-district
    area_weight: 0.0479
  - to: "us/states/pa/districts/house/103"
    rel: in-district
    area_weight: 0.0161
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Dauphin County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 289593 |
| Under 18 | 64718 |
| 18–64 | 172654 |
| 65+ | 52221 |
| Median household income | 76242 |
| Poverty rate | 12.87 |
| Homeownership rate | 63.08 |
| Unemployment rate | 4.51 |
| Median home value | 236400 |
| Gini index | 0.4611 |
| Vacancy rate | 5.06 |
| White | 182570 |
| Black | 49862 |
| Asian | 18938 |
| Native | 832 |
| Hispanic/Latino | 34032 |
| Bachelor's or higher | 95020 |

## Districts

- [PA-10](/us/states/pa/districts/10.md) — 100% (congressional)
- [PA Senate District 15](/us/states/pa/districts/senate/15.md) — 53% (state senate)
- [PA Senate District 34](/us/states/pa/districts/senate/34.md) — 47% (state senate)
- [PA House District 125](/us/states/pa/districts/house/125.md) — 64% (state house)
- [PA House District 106](/us/states/pa/districts/house/106.md) — 24% (state house)
- [PA House District 105](/us/states/pa/districts/house/105.md) — 5% (state house)
- [PA House District 104](/us/states/pa/districts/house/104.md) — 5% (state house)
- [PA House District 103](/us/states/pa/districts/house/103.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
