---
type: Jurisdiction
title: "Orangeburg County, SC"
classification: county
fips: "45075"
state: "SC"
demographics:
  population: 83253
  population_under_18: 17850
  population_18_64: 47988
  population_65_plus: 17415
  median_household_income: 45675
  poverty_rate: 22.44
  homeownership_rate: 66.96
  unemployment_rate: 8.31
  median_home_value: 115800
  gini_index: 0.4919
  vacancy_rate: 20.35
  race_white: 28290
  race_black: 50605
  race_asian: 832
  race_native: 232
  hispanic: 2231
  bachelors_plus: 16145
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.6019
  - to: "us/states/sc/districts/02"
    rel: in-district
    area_weight: 0.3976
  - to: "us/states/sc/districts/senate/40"
    rel: in-district
    area_weight: 0.4522
  - to: "us/states/sc/districts/senate/39"
    rel: in-district
    area_weight: 0.3649
  - to: "us/states/sc/districts/senate/36"
    rel: in-district
    area_weight: 0.1829
  - to: "us/states/sc/districts/house/90"
    rel: in-district
    area_weight: 0.309
  - to: "us/states/sc/districts/house/95"
    rel: in-district
    area_weight: 0.2666
  - to: "us/states/sc/districts/house/91"
    rel: in-district
    area_weight: 0.2401
  - to: "us/states/sc/districts/house/93"
    rel: in-district
    area_weight: 0.1843
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Orangeburg County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83253 |
| Under 18 | 17850 |
| 18–64 | 47988 |
| 65+ | 17415 |
| Median household income | 45675 |
| Poverty rate | 22.44 |
| Homeownership rate | 66.96 |
| Unemployment rate | 8.31 |
| Median home value | 115800 |
| Gini index | 0.4919 |
| Vacancy rate | 20.35 |
| White | 28290 |
| Black | 50605 |
| Asian | 832 |
| Native | 232 |
| Hispanic/Latino | 2231 |
| Bachelor's or higher | 16145 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 60% (congressional)
- [SC-02](/us/states/sc/districts/02.md) — 40% (congressional)
- [SC Senate District 40](/us/states/sc/districts/senate/40.md) — 45% (state senate)
- [SC Senate District 39](/us/states/sc/districts/senate/39.md) — 36% (state senate)
- [SC Senate District 36](/us/states/sc/districts/senate/36.md) — 18% (state senate)
- [SC House District 90](/us/states/sc/districts/house/90.md) — 31% (state house)
- [SC House District 95](/us/states/sc/districts/house/95.md) — 27% (state house)
- [SC House District 91](/us/states/sc/districts/house/91.md) — 24% (state house)
- [SC House District 93](/us/states/sc/districts/house/93.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
