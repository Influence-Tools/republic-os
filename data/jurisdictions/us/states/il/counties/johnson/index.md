---
type: Jurisdiction
title: "Johnson County, IL"
classification: county
fips: "17087"
state: "IL"
demographics:
  population: 13376
  population_under_18: 2483
  population_18_64: 8263
  population_65_plus: 2630
  median_household_income: 62528
  poverty_rate: 17.58
  homeownership_rate: 81.98
  unemployment_rate: 3.48
  median_home_value: 160500
  gini_index: 0.4358
  vacancy_rate: 25.99
  race_white: 10772
  race_black: 1043
  race_asian: 33
  race_native: 0
  hispanic: 597
  bachelors_plus: 2578
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Johnson County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13376 |
| Under 18 | 2483 |
| 18–64 | 8263 |
| 65+ | 2630 |
| Median household income | 62528 |
| Poverty rate | 17.58 |
| Homeownership rate | 81.98 |
| Unemployment rate | 3.48 |
| Median home value | 160500 |
| Gini index | 0.4358 |
| Vacancy rate | 25.99 |
| White | 10772 |
| Black | 1043 |
| Asian | 33 |
| Native | 0 |
| Hispanic/Latino | 597 |
| Bachelor's or higher | 2578 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 117](/us/states/il/districts/house/117.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
