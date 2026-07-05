---
type: Jurisdiction
title: "Atlantic County, NJ"
classification: county
fips: "34001"
state: "NJ"
demographics:
  population: 276270
  population_under_18: 57395
  population_18_64: 164033
  population_65_plus: 54842
  median_household_income: 78050
  poverty_rate: 13.18
  homeownership_rate: 68.71
  unemployment_rate: 8.78
  median_home_value: 295000
  gini_index: 0.4668
  vacancy_rate: 17.13
  race_white: 155037
  race_black: 37110
  race_asian: 21681
  race_native: 1961
  hispanic: 56285
  bachelors_plus: 82793
districts:
  - to: "us/states/nj/districts/02"
    rel: in-district
    area_weight: 0.9057
  - to: "us/states/nj/districts/senate/2"
    rel: in-district
    area_weight: 0.5442
  - to: "us/states/nj/districts/senate/8"
    rel: in-district
    area_weight: 0.1762
  - to: "us/states/nj/districts/senate/1"
    rel: in-district
    area_weight: 0.1134
  - to: "us/states/nj/districts/senate/4"
    rel: in-district
    area_weight: 0.0732
  - to: "us/states/nj/districts/house/2"
    rel: in-district
    area_weight: 0.5442
  - to: "us/states/nj/districts/house/8"
    rel: in-district
    area_weight: 0.1762
  - to: "us/states/nj/districts/house/1"
    rel: in-district
    area_weight: 0.1134
  - to: "us/states/nj/districts/house/4"
    rel: in-district
    area_weight: 0.0732
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Atlantic County, NJ

County jurisdiction — 13 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 276270 |
| Under 18 | 57395 |
| 18–64 | 164033 |
| 65+ | 54842 |
| Median household income | 78050 |
| Poverty rate | 13.18 |
| Homeownership rate | 68.71 |
| Unemployment rate | 8.78 |
| Median home value | 295000 |
| Gini index | 0.4668 |
| Vacancy rate | 17.13 |
| White | 155037 |
| Black | 37110 |
| Asian | 21681 |
| Native | 1961 |
| Hispanic/Latino | 56285 |
| Bachelor's or higher | 82793 |

## Districts

- [NJ-02](/us/states/nj/districts/02.md) — 91% (congressional)
- [NJ Senate District 2](/us/states/nj/districts/senate/2.md) — 54% (state senate)
- [NJ Senate District 8](/us/states/nj/districts/senate/8.md) — 18% (state senate)
- [NJ Senate District 1](/us/states/nj/districts/senate/1.md) — 11% (state senate)
- [NJ Senate District 4](/us/states/nj/districts/senate/4.md) — 7% (state senate)
- [NJ House District 2](/us/states/nj/districts/house/2.md) — 54% (state house)
- [NJ House District 8](/us/states/nj/districts/house/8.md) — 18% (state house)
- [NJ House District 1](/us/states/nj/districts/house/1.md) — 11% (state house)
- [NJ House District 4](/us/states/nj/districts/house/4.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
