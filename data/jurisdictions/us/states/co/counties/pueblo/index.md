---
type: Jurisdiction
title: "Pueblo County, CO"
classification: county
fips: "08101"
state: "CO"
demographics:
  population: 169356
  population_under_18: 36904
  population_18_64: 99045
  population_65_plus: 33407
  median_household_income: 64010
  poverty_rate: 14.6
  homeownership_rate: 68.88
  unemployment_rate: 4.78
  median_home_value: 291300
  gini_index: 0.4531
  vacancy_rate: 6.96
  race_white: 121602
  race_black: 3522
  race_asian: 1522
  race_native: 2968
  hispanic: 71367
  bachelors_plus: 41167
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 0.5836
  - to: "us/states/co/districts/house/46"
    rel: in-district
    area_weight: 0.2815
  - to: "us/states/co/districts/house/60"
    rel: in-district
    area_weight: 0.0786
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 0.0563
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Pueblo County, CO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 169356 |
| Under 18 | 36904 |
| 18–64 | 99045 |
| 65+ | 33407 |
| Median household income | 64010 |
| Poverty rate | 14.6 |
| Homeownership rate | 68.88 |
| Unemployment rate | 4.78 |
| Median home value | 291300 |
| Gini index | 0.4531 |
| Vacancy rate | 6.96 |
| White | 121602 |
| Black | 3522 |
| Asian | 1522 |
| Native | 2968 |
| Hispanic/Latino | 71367 |
| Bachelor's or higher | 41167 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 3](/us/states/co/districts/senate/3.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 58% (state house)
- [CO House District 46](/us/states/co/districts/house/46.md) — 28% (state house)
- [CO House District 60](/us/states/co/districts/house/60.md) — 8% (state house)
- [CO House District 62](/us/states/co/districts/house/62.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
