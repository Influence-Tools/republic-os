---
type: Jurisdiction
title: "Hendry County, FL"
classification: county
fips: "12051"
state: "FL"
demographics:
  population: 42382
  population_under_18: 11783
  population_18_64: 14729
  population_65_plus: 15870
  median_household_income: 56393
  poverty_rate: 22.53
  homeownership_rate: 73.57
  unemployment_rate: 4.39
  median_home_value: 219200
  gini_index: 0.476
  vacancy_rate: 12.5
  race_white: 19973
  race_black: 4805
  race_asian: 489
  race_native: 1290
  hispanic: 24422
  bachelors_plus: 4342
districts:
  - to: "us/states/fl/districts/18"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/fl/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/82"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Hendry County, FL

County jurisdiction — 28 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42382 |
| Under 18 | 11783 |
| 18–64 | 14729 |
| 65+ | 15870 |
| Median household income | 56393 |
| Poverty rate | 22.53 |
| Homeownership rate | 73.57 |
| Unemployment rate | 4.39 |
| Median home value | 219200 |
| Gini index | 0.476 |
| Vacancy rate | 12.5 |
| White | 19973 |
| Black | 4805 |
| Asian | 489 |
| Native | 1290 |
| Hispanic/Latino | 24422 |
| Bachelor's or higher | 4342 |

## Districts

- [FL-18](/us/states/fl/districts/18.md) — 100% (congressional)
- [FL Senate District 28](/us/states/fl/districts/senate/28.md) — 100% (state senate)
- [FL House District 82](/us/states/fl/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
