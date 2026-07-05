---
type: Jurisdiction
title: "White County, AR"
classification: county
fips: "05145"
state: "AR"
demographics:
  population: 77838
  population_under_18: 18039
  population_18_64: 46599
  population_65_plus: 13200
  median_household_income: 55249
  poverty_rate: 17.55
  homeownership_rate: 69.13
  unemployment_rate: 5.81
  median_home_value: 163600
  gini_index: 0.452
  vacancy_rate: 12.6
  race_white: 67907
  race_black: 3326
  race_asian: 539
  race_native: 146
  hispanic: 3853
  bachelors_plus: 14866
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 0.9957
  - to: "us/states/ar/districts/senate/18"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ar/districts/house/57"
    rel: in-district
    area_weight: 0.2877
  - to: "us/states/ar/districts/house/39"
    rel: in-district
    area_weight: 0.2693
  - to: "us/states/ar/districts/house/59"
    rel: in-district
    area_weight: 0.2222
  - to: "us/states/ar/districts/house/40"
    rel: in-district
    area_weight: 0.1422
  - to: "us/states/ar/districts/house/58"
    rel: in-district
    area_weight: 0.0783
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# White County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 77838 |
| Under 18 | 18039 |
| 18–64 | 46599 |
| 65+ | 13200 |
| Median household income | 55249 |
| Poverty rate | 17.55 |
| Homeownership rate | 69.13 |
| Unemployment rate | 5.81 |
| Median home value | 163600 |
| Gini index | 0.452 |
| Vacancy rate | 12.6 |
| White | 67907 |
| Black | 3326 |
| Asian | 539 |
| Native | 146 |
| Hispanic/Latino | 3853 |
| Bachelor's or higher | 14866 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 18](/us/states/ar/districts/senate/18.md) — 100% (state senate)
- [AR House District 57](/us/states/ar/districts/house/57.md) — 29% (state house)
- [AR House District 39](/us/states/ar/districts/house/39.md) — 27% (state house)
- [AR House District 59](/us/states/ar/districts/house/59.md) — 22% (state house)
- [AR House District 40](/us/states/ar/districts/house/40.md) — 14% (state house)
- [AR House District 58](/us/states/ar/districts/house/58.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
