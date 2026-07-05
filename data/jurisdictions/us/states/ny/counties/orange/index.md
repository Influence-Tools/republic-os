---
type: Jurisdiction
title: "Orange County, NY"
classification: county
fips: "36071"
state: "NY"
demographics:
  population: 406616
  population_under_18: 104187
  population_18_64: 242894
  population_65_plus: 59535
  median_household_income: 97178
  poverty_rate: 12.64
  homeownership_rate: 67.82
  unemployment_rate: 5.47
  median_home_value: 387900
  gini_index: 0.4489
  vacancy_rate: 7.41
  race_white: 251943
  race_black: 47046
  race_asian: 11920
  race_native: 4226
  hispanic: 97218
  bachelors_plus: 121306
districts:
  - to: "us/states/ny/districts/18"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ny/districts/senate/42"
    rel: in-district
    area_weight: 0.8767
  - to: "us/states/ny/districts/senate/39"
    rel: in-district
    area_weight: 0.123
  - to: "us/states/ny/districts/house/98"
    rel: in-district
    area_weight: 0.4172
  - to: "us/states/ny/districts/house/101"
    rel: in-district
    area_weight: 0.2659
  - to: "us/states/ny/districts/house/99"
    rel: in-district
    area_weight: 0.1737
  - to: "us/states/ny/districts/house/100"
    rel: in-district
    area_weight: 0.0812
  - to: "us/states/ny/districts/house/104"
    rel: in-district
    area_weight: 0.0618
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Orange County, NY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 406616 |
| Under 18 | 104187 |
| 18–64 | 242894 |
| 65+ | 59535 |
| Median household income | 97178 |
| Poverty rate | 12.64 |
| Homeownership rate | 67.82 |
| Unemployment rate | 5.47 |
| Median home value | 387900 |
| Gini index | 0.4489 |
| Vacancy rate | 7.41 |
| White | 251943 |
| Black | 47046 |
| Asian | 11920 |
| Native | 4226 |
| Hispanic/Latino | 97218 |
| Bachelor's or higher | 121306 |

## Districts

- [NY-18](/us/states/ny/districts/18.md) — 100% (congressional)
- [NY Senate District 42](/us/states/ny/districts/senate/42.md) — 88% (state senate)
- [NY Senate District 39](/us/states/ny/districts/senate/39.md) — 12% (state senate)
- [NY House District 98](/us/states/ny/districts/house/98.md) — 42% (state house)
- [NY House District 101](/us/states/ny/districts/house/101.md) — 27% (state house)
- [NY House District 99](/us/states/ny/districts/house/99.md) — 17% (state house)
- [NY House District 100](/us/states/ny/districts/house/100.md) — 8% (state house)
- [NY House District 104](/us/states/ny/districts/house/104.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
