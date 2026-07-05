---
type: Jurisdiction
title: "Okaloosa County, FL"
classification: county
fips: "12091"
state: "FL"
demographics:
  population: 216599
  population_under_18: 48926
  population_18_64: 131626
  population_65_plus: 36047
  median_household_income: 81998
  poverty_rate: 9.32
  homeownership_rate: 68.4
  unemployment_rate: 3.81
  median_home_value: 351200
  gini_index: 0.439
  vacancy_rate: 17.77
  race_white: 155735
  race_black: 20101
  race_asian: 7442
  race_native: 691
  hispanic: 24572
  bachelors_plus: 72728
districts:
  - to: "us/states/fl/districts/01"
    rel: in-district
    area_weight: 0.7996
  - to: "us/states/fl/districts/senate/2"
    rel: in-district
    area_weight: 0.522
  - to: "us/states/fl/districts/senate/1"
    rel: in-district
    area_weight: 0.2766
  - to: "us/states/fl/districts/house/4"
    rel: in-district
    area_weight: 0.4579
  - to: "us/states/fl/districts/house/3"
    rel: in-district
    area_weight: 0.3406
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Okaloosa County, FL

County jurisdiction — 68 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 216599 |
| Under 18 | 48926 |
| 18–64 | 131626 |
| 65+ | 36047 |
| Median household income | 81998 |
| Poverty rate | 9.32 |
| Homeownership rate | 68.4 |
| Unemployment rate | 3.81 |
| Median home value | 351200 |
| Gini index | 0.439 |
| Vacancy rate | 17.77 |
| White | 155735 |
| Black | 20101 |
| Asian | 7442 |
| Native | 691 |
| Hispanic/Latino | 24572 |
| Bachelor's or higher | 72728 |

## Districts

- [FL-01](/us/states/fl/districts/01.md) — 80% (congressional)
- [FL Senate District 2](/us/states/fl/districts/senate/2.md) — 52% (state senate)
- [FL Senate District 1](/us/states/fl/districts/senate/1.md) — 28% (state senate)
- [FL House District 4](/us/states/fl/districts/house/4.md) — 46% (state house)
- [FL House District 3](/us/states/fl/districts/house/3.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
