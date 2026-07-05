---
type: Jurisdiction
title: "Richland County, IL"
classification: county
fips: "17159"
state: "IL"
demographics:
  population: 15598
  population_under_18: 3584
  population_18_64: 8780
  population_65_plus: 3234
  median_household_income: 62455
  poverty_rate: 12.08
  homeownership_rate: 73.75
  unemployment_rate: 3.12
  median_home_value: 112000
  gini_index: 0.4228
  vacancy_rate: 12.49
  race_white: 14630
  race_black: 68
  race_asian: 85
  race_native: 9
  hispanic: 309
  bachelors_plus: 2711
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/house/110"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Richland County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15598 |
| Under 18 | 3584 |
| 18–64 | 8780 |
| 65+ | 3234 |
| Median household income | 62455 |
| Poverty rate | 12.08 |
| Homeownership rate | 73.75 |
| Unemployment rate | 3.12 |
| Median home value | 112000 |
| Gini index | 0.4228 |
| Vacancy rate | 12.49 |
| White | 14630 |
| Black | 68 |
| Asian | 85 |
| Native | 9 |
| Hispanic/Latino | 309 |
| Bachelor's or higher | 2711 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 100% (state senate)
- [IL House District 110](/us/states/il/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
