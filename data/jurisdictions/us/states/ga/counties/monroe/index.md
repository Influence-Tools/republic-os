---
type: Jurisdiction
title: "Monroe County, GA"
classification: county
fips: "13207"
state: "GA"
demographics:
  population: 29664
  population_under_18: 6267
  population_18_64: 17720
  population_65_plus: 5677
  median_household_income: 83183
  poverty_rate: 12.32
  homeownership_rate: 83.77
  unemployment_rate: 2.69
  median_home_value: 271200
  gini_index: 0.469
  vacancy_rate: 8.84
  race_white: 21679
  race_black: 6565
  race_asian: 356
  race_native: 96
  hispanic: 853
  bachelors_plus: 7974
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ga/districts/senate/18"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/145"
    rel: in-district
    area_weight: 0.4971
  - to: "us/states/ga/districts/house/118"
    rel: in-district
    area_weight: 0.4411
  - to: "us/states/ga/districts/house/144"
    rel: in-district
    area_weight: 0.0612
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Monroe County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29664 |
| Under 18 | 6267 |
| 18–64 | 17720 |
| 65+ | 5677 |
| Median household income | 83183 |
| Poverty rate | 12.32 |
| Homeownership rate | 83.77 |
| Unemployment rate | 2.69 |
| Median home value | 271200 |
| Gini index | 0.469 |
| Vacancy rate | 8.84 |
| White | 21679 |
| Black | 6565 |
| Asian | 356 |
| Native | 96 |
| Hispanic/Latino | 853 |
| Bachelor's or higher | 7974 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 18](/us/states/ga/districts/senate/18.md) — 100% (state senate)
- [GA House District 145](/us/states/ga/districts/house/145.md) — 50% (state house)
- [GA House District 118](/us/states/ga/districts/house/118.md) — 44% (state house)
- [GA House District 144](/us/states/ga/districts/house/144.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
