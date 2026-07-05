---
type: Jurisdiction
title: "Patrick County, VA"
classification: county
fips: "51141"
state: "VA"
demographics:
  population: 17512
  population_under_18: 3047
  population_18_64: 9630
  population_65_plus: 4835
  median_household_income: 53038
  poverty_rate: 11.67
  homeownership_rate: 76.92
  unemployment_rate: 2.5
  median_home_value: 153400
  gini_index: 0.4557
  vacancy_rate: 22.37
  race_white: 15670
  race_black: 884
  race_asian: 90
  race_native: 8
  hispanic: 615
  bachelors_plus: 2543
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/47"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Patrick County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17512 |
| Under 18 | 3047 |
| 18–64 | 9630 |
| 65+ | 4835 |
| Median household income | 53038 |
| Poverty rate | 11.67 |
| Homeownership rate | 76.92 |
| Unemployment rate | 2.5 |
| Median home value | 153400 |
| Gini index | 0.4557 |
| Vacancy rate | 22.37 |
| White | 15670 |
| Black | 884 |
| Asian | 90 |
| Native | 8 |
| Hispanic/Latino | 615 |
| Bachelor's or higher | 2543 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 100% (state senate)
- [VA House District 47](/us/states/va/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
