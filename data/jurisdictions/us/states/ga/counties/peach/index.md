---
type: Jurisdiction
title: "Peach County, GA"
classification: county
fips: "13225"
state: "GA"
demographics:
  population: 28560
  population_under_18: 6076
  population_18_64: 17705
  population_65_plus: 4779
  median_household_income: 71293
  poverty_rate: 17.34
  homeownership_rate: 69.56
  unemployment_rate: 6.62
  median_home_value: 207800
  gini_index: 0.4503
  vacancy_rate: 13.46
  race_white: 13211
  race_black: 11873
  race_asian: 109
  race_native: 46
  hispanic: 2674
  bachelors_plus: 6323
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9974
  - to: "us/states/ga/districts/senate/18"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/150"
    rel: in-district
    area_weight: 0.5162
  - to: "us/states/ga/districts/house/147"
    rel: in-district
    area_weight: 0.2759
  - to: "us/states/ga/districts/house/134"
    rel: in-district
    area_weight: 0.2078
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Peach County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28560 |
| Under 18 | 6076 |
| 18–64 | 17705 |
| 65+ | 4779 |
| Median household income | 71293 |
| Poverty rate | 17.34 |
| Homeownership rate | 69.56 |
| Unemployment rate | 6.62 |
| Median home value | 207800 |
| Gini index | 0.4503 |
| Vacancy rate | 13.46 |
| White | 13211 |
| Black | 11873 |
| Asian | 109 |
| Native | 46 |
| Hispanic/Latino | 2674 |
| Bachelor's or higher | 6323 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 18](/us/states/ga/districts/senate/18.md) — 100% (state senate)
- [GA House District 150](/us/states/ga/districts/house/150.md) — 52% (state house)
- [GA House District 147](/us/states/ga/districts/house/147.md) — 28% (state house)
- [GA House District 134](/us/states/ga/districts/house/134.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
