---
type: Jurisdiction
title: "Sedgwick County, CO"
classification: county
fips: "08115"
state: "CO"
demographics:
  population: 2304
  population_under_18: 580
  population_18_64: 646
  population_65_plus: 1078
  median_household_income: 52386
  poverty_rate: 13.05
  homeownership_rate: 71.82
  unemployment_rate: 2.94
  median_home_value: 149000
  gini_index: 0.4415
  vacancy_rate: 15.82
  race_white: 1861
  race_black: 22
  race_asian: 41
  race_native: 2
  hispanic: 446
  bachelors_plus: 575
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Sedgwick County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2304 |
| Under 18 | 580 |
| 18–64 | 646 |
| 65+ | 1078 |
| Median household income | 52386 |
| Poverty rate | 13.05 |
| Homeownership rate | 71.82 |
| Unemployment rate | 2.94 |
| Median home value | 149000 |
| Gini index | 0.4415 |
| Vacancy rate | 15.82 |
| White | 1861 |
| Black | 22 |
| Asian | 41 |
| Native | 2 |
| Hispanic/Latino | 446 |
| Bachelor's or higher | 575 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 100% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
