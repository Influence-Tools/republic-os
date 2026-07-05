---
type: Jurisdiction
title: "Coffee County, GA"
classification: county
fips: "13069"
state: "GA"
demographics:
  population: 43347
  population_under_18: 10640
  population_18_64: 26389
  population_65_plus: 6318
  median_household_income: 50683
  poverty_rate: 23.15
  homeownership_rate: 64.66
  unemployment_rate: 4.37
  median_home_value: 128900
  gini_index: 0.4807
  vacancy_rate: 12.27
  race_white: 25735
  race_black: 12170
  race_asian: 319
  race_native: 160
  hispanic: 5861
  bachelors_plus: 5797
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 0.5512
  - to: "us/states/ga/districts/senate/19"
    rel: in-district
    area_weight: 0.4486
  - to: "us/states/ga/districts/house/169"
    rel: in-district
    area_weight: 0.8318
  - to: "us/states/ga/districts/house/176"
    rel: in-district
    area_weight: 0.1679
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Coffee County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43347 |
| Under 18 | 10640 |
| 18–64 | 26389 |
| 65+ | 6318 |
| Median household income | 50683 |
| Poverty rate | 23.15 |
| Homeownership rate | 64.66 |
| Unemployment rate | 4.37 |
| Median home value | 128900 |
| Gini index | 0.4807 |
| Vacancy rate | 12.27 |
| White | 25735 |
| Black | 12170 |
| Asian | 319 |
| Native | 160 |
| Hispanic/Latino | 5861 |
| Bachelor's or higher | 5797 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 55% (state senate)
- [GA Senate District 19](/us/states/ga/districts/senate/19.md) — 45% (state senate)
- [GA House District 169](/us/states/ga/districts/house/169.md) — 83% (state house)
- [GA House District 176](/us/states/ga/districts/house/176.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
