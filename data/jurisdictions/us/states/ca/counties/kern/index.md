---
type: Jurisdiction
title: "Kern County, CA"
classification: county
fips: "06029"
state: "CA"
demographics:
  population: 915075
  population_under_18: 261490
  population_18_64: 545025
  population_65_plus: 108560
  median_household_income: 70210
  poverty_rate: 19.11
  homeownership_rate: 60.06
  unemployment_rate: 8.63
  median_home_value: 338300
  gini_index: 0.4584
  vacancy_rate: 7.19
  race_white: 402035
  race_black: 46662
  race_asian: 48277
  race_native: 12240
  hispanic: 516662
  bachelors_plus: 142335
districts:
  - to: "us/states/ca/districts/20"
    rel: in-district
    area_weight: 0.6475
  - to: "us/states/ca/districts/22"
    rel: in-district
    area_weight: 0.2685
  - to: "us/states/ca/districts/23"
    rel: in-district
    area_weight: 0.0839
  - to: "us/states/ca/districts/senate/12"
    rel: in-district
    area_weight: 0.799
  - to: "us/states/ca/districts/senate/16"
    rel: in-district
    area_weight: 0.2009
  - to: "us/states/ca/districts/house/32"
    rel: in-district
    area_weight: 0.5959
  - to: "us/states/ca/districts/house/35"
    rel: in-district
    area_weight: 0.2315
  - to: "us/states/ca/districts/house/34"
    rel: in-district
    area_weight: 0.1725
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Kern County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 915075 |
| Under 18 | 261490 |
| 18–64 | 545025 |
| 65+ | 108560 |
| Median household income | 70210 |
| Poverty rate | 19.11 |
| Homeownership rate | 60.06 |
| Unemployment rate | 8.63 |
| Median home value | 338300 |
| Gini index | 0.4584 |
| Vacancy rate | 7.19 |
| White | 402035 |
| Black | 46662 |
| Asian | 48277 |
| Native | 12240 |
| Hispanic/Latino | 516662 |
| Bachelor's or higher | 142335 |

## Districts

- [CA-20](/us/states/ca/districts/20.md) — 65% (congressional)
- [CA-22](/us/states/ca/districts/22.md) — 27% (congressional)
- [CA-23](/us/states/ca/districts/23.md) — 8% (congressional)
- [CA Senate District 12](/us/states/ca/districts/senate/12.md) — 80% (state senate)
- [CA Senate District 16](/us/states/ca/districts/senate/16.md) — 20% (state senate)
- [CA House District 32](/us/states/ca/districts/house/32.md) — 60% (state house)
- [CA House District 35](/us/states/ca/districts/house/35.md) — 23% (state house)
- [CA House District 34](/us/states/ca/districts/house/34.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
