---
type: Jurisdiction
title: "Kauai County, HI"
classification: county
fips: "15007"
state: "HI"
demographics:
  population: 73731
  population_under_18: 15636
  population_18_64: 41565
  population_65_plus: 16530
  median_household_income: 97668
  poverty_rate: 9.09
  homeownership_rate: 68.59
  unemployment_rate: 3.85
  median_home_value: 873200
  gini_index: 0.446
  vacancy_rate: 22.44
  race_white: 21863
  race_black: 639
  race_asian: 22560
  race_native: 146
  hispanic: 7804
  bachelors_plus: 21597
districts:
  - to: "us/states/hi/districts/02"
    rel: in-district
    area_weight: 0.4937
  - to: "us/states/hi/districts/senate/8"
    rel: in-district
    area_weight: 0.4972
  - to: "us/states/hi/districts/house/17"
    rel: in-district
    area_weight: 0.2699
  - to: "us/states/hi/districts/house/15"
    rel: in-district
    area_weight: 0.1482
  - to: "us/states/hi/districts/house/16"
    rel: in-district
    area_weight: 0.0791
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, hi]
timestamp: "2026-07-03"
---

# Kauai County, HI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 73731 |
| Under 18 | 15636 |
| 18–64 | 41565 |
| 65+ | 16530 |
| Median household income | 97668 |
| Poverty rate | 9.09 |
| Homeownership rate | 68.59 |
| Unemployment rate | 3.85 |
| Median home value | 873200 |
| Gini index | 0.446 |
| Vacancy rate | 22.44 |
| White | 21863 |
| Black | 639 |
| Asian | 22560 |
| Native | 146 |
| Hispanic/Latino | 7804 |
| Bachelor's or higher | 21597 |

## Districts

- [HI-02](/us/states/hi/districts/02.md) — 49% (congressional)
- [HI Senate District 8](/us/states/hi/districts/senate/8.md) — 50% (state senate)
- [HI House District 17](/us/states/hi/districts/house/17.md) — 27% (state house)
- [HI House District 15](/us/states/hi/districts/house/15.md) — 15% (state house)
- [HI House District 16](/us/states/hi/districts/house/16.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
